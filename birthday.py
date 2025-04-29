from field import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, value):
        try:
            # Validate format (but keep the original string)
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)
