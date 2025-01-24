import platform

from pygfdrivers.common.usb_scope import UsbScope
from pygfdrivers.common.visa_scope import VisaScope
from pygfdrivers.common.util.utilities import has_prop, has_setter
from pygfdrivers.common.base_command import VisaCommand, UsbCommand

from pygfdrivers.gf.util.utilities import (
    format_start,
    format_channel,
    format_averages,
    format_num_points,
)

from gf_data_models.gf.digitizer.digitizer import GfCaptureModel

# Determine the base class based on the platform
if platform.system() == "Linux":
    ScopeClass = UsbScope
    CommandClass = UsbCommand
elif platform.system() == "Windows":
    ScopeClass = VisaScope
    CommandClass = VisaCommand
else:
    raise RuntimeError("Unsupported platform")


class GFDigitizerCapture(CommandClass):
    def __init__(self, scope: ScopeClass) -> None:
        super().__init__(scope)
        self._acq_srate = scope.config.capture.acq_srate
        self._acq_bit_res = 12

    def apply_capture_config(self, config: GfCaptureModel) -> None:
        try:  
            for field, setting in config.model_dump().items():
                if has_setter(self, field) and setting is not None:
                    self.log.debug(f"Setting '{field}' to '{setting}'.")
                    setattr(self, field, setting)

        except Exception as e:
            self.log.error(f"Applying capture configuration encountered error: {e}")
            raise

    def fetch_capture_config(self, config: GfCaptureModel) -> None:
        try:
            for field in self.capture_fields:
                if has_prop(self, field):
                    setattr(config, field, getattr(self, field))

        except Exception as e:
            self.log.error(f"Fetching capture configuration encountered error: {e}")

    def get_data(self, channel: int, averages: int = None, start: int = None, points: int = None) -> None:
        # TODO: Add check that 'points' or number of samples being requested from digitizer is within 0 to 256K
        # Safe max number of points saved by the digitizer is 256K points per channel regardless of sample rate.

        channel = format_channel(channel)
        start = format_start(start or self.acq_start_sample)
        averages = format_averages(averages or self.acq_count)
        points = format_num_points(points or self.acq_total_samples)
        self.write(cmd=f"readdata chan={channel} avgs={averages} start={start} number={points}")

    @property
    def acq_bit_res(self) -> int:
        return self._acq_bit_res

    @acq_bit_res.setter
    def acq_bit_res(self, bit_res: int) -> None:
        self._acq_bit_res = bit_res

    @property
    def acq_count(self) -> int:
        return self._samples_to_avg
    
    @acq_count.setter
    def acq_count(self, count: int) -> None:
        self._samples_to_avg = count

    @property
    def time_range(self) -> float:
        return self._time_range
    
    @time_range.setter
    def time_range(self, t_range: int) -> None:
        num_points = t_range * self.acq_srate

        if num_points % 32 != 0:
            num_points = (num_points // 32) * 32
            t_range = num_points / self.acq_srate

        self._time_range = t_range

    @property
    def time_zero(self) -> float:
        return self._time_zero
    
    @time_zero.setter
    def time_zero(self, value: float) -> None:
        self._time_zero = value

    @property
    def volt_range(self) -> float:
        return self._volt_range
    
    @volt_range.setter
    def volt_range(self, v_range: float) -> None:
        self._volt_range = v_range

    @property
    def acq_total_samples(self) -> int:
        _samples = int(self.acq_srate * self.time_range)
        return _samples
    
    @acq_total_samples.setter
    def acq_total_samples(self, samples: int) -> None:
        self.time_range = int(samples / self.acq_srate)

    @property
    def acq_start_sample(self) -> int:
        _start = int(self.acq_srate * self.time_zero)
        return _start
    
    @acq_start_sample.setter
    def acq_start_sample(self, start: int) -> None:
        self.time_zero = float(start / self.acq_srate)

    @property
    def acq_srate(self) -> float:
        return self._acq_srate
