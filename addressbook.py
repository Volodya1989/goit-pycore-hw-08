from collections import UserDict
from datetime import date, timedelta, datetime


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)

    def get_upcoming_birthdays(self, days=7):
        upcoming = []
        today = date.today()
        for record in self.data.values():
            if record.birthday:
                # Parse the birthday string into a date object
                try:
                    bday = datetime.strptime(
                        record.birthday.value, "%d.%m.%Y").date()
                except ValueError:
                    continue  # Skip if the date is invalid

                birthday_this_year = bday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(
                        year=today.year + 1)

                if birthday_this_year.weekday() in (5, 6):  # Saturday or Sunday
                    birthday_this_year += timedelta(
                        days=(7 - birthday_this_year.weekday()))

                days_until_birthday = (birthday_this_year - today).days

                if 0 <= days_until_birthday <= days:
                    upcoming.append({
                        "name": record.name.value,
                        "birthday": birthday_this_year.strftime("%d.%m.%Y")
                    })
        return upcoming
