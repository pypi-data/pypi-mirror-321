import sys
import logging
import colorama

colorama.init(strip=True)


class LOGGING_MODE:
    DEBUG   = 1
    INFO    = 2


class PyVisaFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return not record.name.startswith('pyvisa')

class TimerLogger(logging.Logger):
    TIMER_LEVEL = 25

    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        logging.addLevelName(self.TIMER_LEVEL, 'TIMER')
        logging.basicConfig(stream=sys.stdout)

    def timer(self, message, *args, **kwargs):
        if self.isEnabledFor(self.TIMER_LEVEL):
            self.log(self.TIMER_LEVEL, message, *args, **kwargs)


# Set TimerLogger as the logger class
logging.setLoggerClass(TimerLogger)

class LoggerManager:
    def __init__(self, name: str, mode: int, shot_num: str = None) -> None:
        self.name = name
        self.shot_num = shot_num
        self.log = self.setup_logger(mode)

    def setup_logger(self, mode: int = LOGGING_MODE.DEBUG) -> logging.Logger:
        logger = logging.getLogger(self.name)
        logger.propagate = False

        if mode == LOGGING_MODE.DEBUG:
            logger.setLevel(logging.DEBUG)
        elif mode == LOGGING_MODE.INFO:
            logger.setLevel(logging.INFO)

        if not logger.handlers:
            handler = logging.StreamHandler(stream=sys.stdout)
            formatter = logging.Formatter(self._generate_msg_format())
            handler.setFormatter(LogFormatter(formatter))
            handler.addFilter(PyVisaFilter())
            logger.addHandler(handler)

        return logger

    def update_shot_number(self, shot_number: str = None) -> None:
        self.shot_num = shot_number
        self._update_formatters()

    def _generate_msg_format(self) -> str:
        shot_str = f"[SHOT: {self.shot_num}] " if self.shot_num else ""
        return f"[%(levelname)s] {shot_str}- %(asctime)s - [{self.name}] - %(msg)s"

    def _update_formatters(self) -> None:
        msg_format = self._generate_msg_format()

        for handler in self.log.handlers:
            if isinstance(handler.formatter, logging.Formatter):
                formatter = logging.Formatter(msg_format)
                handler.setFormatter(LogFormatter(formatter))

class LogFormatter(logging.Formatter):
    def __init__(self, formatter: logging.Formatter) -> None:
        super().__init__()
        self.formatter = formatter

    def format(self, record: logging.LogRecord) -> str:
        colors = {
            'DEBUG'     : colorama.Fore.BLUE,
            'INFO'      : colorama.Fore.GREEN,
            'TIMER'     : colorama.Fore.LIGHTCYAN_EX,
            'WARNING'   : colorama.Fore.YELLOW,
            'ERROR'     : colorama.Fore.RED,
            'CRITICAL'  : colorama.Fore.RED,
        }

        color = colors.get(record.levelname, '')
        msg = self.formatter.format(record)
        log_msg = f"{color}{msg}{colorama.Style.RESET_ALL}"

        return log_msg
