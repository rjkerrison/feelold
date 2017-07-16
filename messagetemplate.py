from datetime import datetime
from string import Formatter

class MessageTemplate(str):
    def __init__(self, message):
        self.message = message
        self.replacements = self._get_replacements()

    def __new__(self,  message):
        return str.__new__(self, message)

    def _get_replacements(self):
        # https://stackoverflow.com/a/25997051/4099675
        formatter = Formatter()
        return [fname for _, fname, _, _ in formatter.parse(self.message) if fname]