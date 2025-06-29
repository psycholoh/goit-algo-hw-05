def parse_input(user_input):
    return user_input.strip().split()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

@input_error
def add_contact(command_parts, contacts):
    name, phone = command_parts[1], command_parts[2]
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(command_parts, contacts):
    name, phone = command_parts[1], command_parts[2]
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(command_parts, contacts):
    name = command_parts[1]
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input(">>> ")
        command_parts = parse_input(user_input)

        if not command_parts:
            print("Invalid command.")
            continue

        command = command_parts[0].lower()
        result = ""

        if command == "add":
            result = add_contact(command_parts, contacts)
        elif command == "change":
            result = change_contact(command_parts, contacts)
        elif command == "phone":
            result = show_phone(command_parts, contacts)
        elif command == "all":
            result = show_all(contacts)
        elif command in ["exit", "close"]:
            print("Good bye!")
            break
        else:
            result = "Unknown command."

        if result:
            print(result)








if __name__ == "__main__":
    main()







