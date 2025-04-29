from addressbook import AddressBook, load_data, save_data
from assistant_bot import add_birthday, parse_input, change_contact, show_all, show_birthday, add_contact, show_phone, birthdays


def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            print("Please enter a command.")
            continue  # Skip to next loop

        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Saving your address book...")
                save_data(book)
                print("Good bye!")

                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(show_phone(args, book))
            case "all":
                print(show_all(book))
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                print(birthdays(args, book))
            case _:
                print("Invalid command.")
        

if __name__ == "__main__":
    main()
