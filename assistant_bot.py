from addressbook import AddressBook
from record import Record


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me valid contact."
        except IndexError:
            return "Not enough parameters. Please  try again."
        except TypeError:
            return "Unexpected input. Please try again."

    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Phone number updated."
    return f"Contact {name} was not found."


@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        return f"{name}: {'; '.join(p.value for p in record.phones)}"
    return f"Contact {name} not found."


@input_error
def show_all(book: AddressBook):
    if not book.data:
        return "No contacts found."
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book):
    name, bday = args
    record = book.find(name)
    if record:
        record.add_birthday(bday)
        return "Birthday added."
    return "Contact not found."


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
          return f"{name}'s birthday is {record.birthday.value}"
    return f"No birthday found for {name}."



@input_error
def birthdays(_, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join([f"{entry['name']}: {entry['birthday']}" for entry in upcoming])
