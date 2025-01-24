from abc import ABC
from pydantic import BaseModel
from usb.core import Device, find
from typing import List, Tuple, Any, Callable, Optional
from usb.util import (
    get_string,
    ENDPOINT_IN,
    ENDPOINT_OUT,
    claim_interface,
    release_interface,
    endpoint_direction,
)

from pygfdrivers.common.base_scope import BaseScope

MAX_BUFFER_SIZE = 64


class UsbScope(BaseScope, ABC):
    def __init__(self, scope_config: BaseModel) -> None:
        super().__init__(scope_config)

        self.scope = None
        self.rx_endpoint = None
        self.tx_endpoint = None
        self.interface_num = 0

        self.vendor_id = self.config.device.usb_vendor_id
        self.product_id = self.config.device.usb_model_code
        self.serial_num = self.config.device.usb_serial_number

    def __getattribute__(self, name: str) -> Any:
        if name in {'_handle_err', 'log'} or name.startswith('__'):
            return super().__getattribute__(name)

        attr = super().__getattribute__(name)

        if callable(attr):
            return lambda *args, **kwargs: self._handle_err(attr, *args, **kwargs)

        return attr

    def init(self) -> None:
        scope = self.connect()

        if scope:
            self.is_connected = True
            scope.set_configuration()
            self._detach_kernel_driver(scope, self.interface_num)
            claim_interface(scope, 0)
            self.scope = scope
        else:
            self.is_connected = False
            raise ConnectionError(f"Failed to connect to USB scope "
                                  f"Vendor ID: {str(self.vendor_id).upper()}, "
                                  f"Product ID: {str(self.product_id).upper()}, "
                                  f"Serial Number: {self.serial_num}.")

    def connect(self, serial_num: str = None) -> Device:
        serial_num = serial_num or self.serial_num
        self.log.info(f"Connecting to USB device serial number {self.serial_num}...")
        usb_scopes = self.find_usb_scopes()

        for usb_scope in usb_scopes:
            device_serial_num = get_string(usb_scope, usb_scope.iSerialNumber)

            if device_serial_num == serial_num:
                self.log.info(f"Connected to USB device serial number: {device_serial_num}")
                self.rx_endpoint, self.tx_endpoint = self.find_endpoints(usb_scope)
                return usb_scope

        raise ValueError(f"No USB devices found with serial number: {serial_num}.")

    def disconnect(self, usb_scope: Device = None) -> None:
        usb_scope = usb_scope or self.scope

        if usb_scope:
            release_interface(self.scope, self.interface_num)
            self._detach_kernel_driver(usb_scope, self.interface_num)

            self.scope = None
            self.log.info(f"USB device disconnected")
        else:
            raise ValueError("No USB device is connected.")

    def find_usb_scopes(self, vendor_id: str = None, product_id: str = None) -> List:
        vendor_id = vendor_id or self.vendor_id
        product_id = product_id or self.product_id
        devices = find(find_all=True, idVendor=int(vendor_id, 16), idProduct=int(product_id, 16))
        return devices

    def find_endpoints(self, usb_scope: Device) -> Tuple:
        usb_scope = usb_scope or self.scope

        bulk_in_endpoint = None
        bulk_out_endpoint = None
        usb_scope.set_configuration()
        config = usb_scope.get_active_configuration()

        for interface in config:
            self._detach_kernel_driver(usb_scope, self.interface_num)

            for endpoint in interface:
                endpoint_attr = endpoint.bmAttributes
                endpoint_addr = endpoint.bEndpointAddress

                # Check if the endpoint is bulk
                if (endpoint_attr & 0x03) == 0x02:
                    if endpoint_direction(endpoint_addr) == ENDPOINT_IN:
                        bulk_in_endpoint = endpoint_addr
                    elif endpoint_direction(endpoint_addr) == ENDPOINT_OUT:
                        bulk_out_endpoint = endpoint_addr

                # Break the loop if both endpoints are found
                if bulk_in_endpoint and bulk_out_endpoint:
                    break

        return bulk_in_endpoint, bulk_out_endpoint

    # ------------------------------------------------------------------------------------
    #  USB Command Handler Methods
    # ------------------------------------------------------------------------------------

    def read_bytes_from_scope(self, num_bytes: int) -> bytes:
        self.log.debug(f"Reading {num_bytes} bytes from scope.")
        byte_data = self.scope.read(self.rx_endpoint, num_bytes)
        return bytes(byte_data)

    def write_scope(self, cmd: str) -> None:
        self.log.debug(f"Writing '{cmd}' to scope.")
        self.scope.write(self.tx_endpoint, cmd.encode('ascii'))

    def query_scope(self, cmd: str) -> Optional[str]:
        self.log.debug(f"Querying '{cmd}' on scope.")
        self.write_scope(cmd)
        response = self.scope.read(self.rx_endpoint, MAX_BUFFER_SIZE)
        response = response.tobytes().decode('ascii')
        return response

    # ------------------------------------------------------------------------------------
    #  Helper Methods
    # ------------------------------------------------------------------------------------

    def _handle_err(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Optional[Any]:
        try:
            ret = func(*args, **kwargs)
            return ret
        except Exception as e:
            self.log.error(f"{func.__name__} encountered error: {repr(e)}")
            return None

    def _detach_kernel_driver(self, usb_scope: Device, interface_number: int) -> None:
        self.log.debug(f"Detaching kernel driver for USB scope {usb_scope} interface {interface_number}...")
        if usb_scope.is_kernel_driver_active(interface_number):
            usb_scope.detach_kernel_driver(interface_number)
