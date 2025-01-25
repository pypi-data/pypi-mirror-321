import datetime

class Logger:
    def __init__(self):
        self.prefix = "CLORE GigaSPOT"

    def _get_timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _color_text(self, text, color):
        colors = {
            "warning": "\033[93m",
            "error": "\033[91m",
            "debug": "\033[92m",
            "reset": "\033[0m",
            "info": "\033[94m",
        }
        return f"{colors.get(color, colors['reset'])}{text}{colors['reset']}"

    def log(self, message):
        print(f"{self._get_timestamp()} | {self.prefix} | {self._color_text('INFO', 'info')} | {message}")

    def warn(self, message):
        print(f"{self._get_timestamp()} | {self.prefix} | {self._color_text('WARNING', 'warning')} | {message}")

    def error(self, message):
        print(f"{self._get_timestamp()} | {self.prefix} | {self._color_text('ERROR', 'error')} | {message}")

    def debug(self, message):
        print(f"{self._get_timestamp()} | {self.prefix} | {self._color_text('DEBUG', 'debug')} | {message}")