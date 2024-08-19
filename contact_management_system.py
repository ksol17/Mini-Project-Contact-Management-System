import os
import re

# Initialize the contacts dictionary
contacts = {}

# Regex patterns for validation
phone_pattern = re.compile(r"^\+?[0-9]{10,15}$")
email_pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

def get_valid_input(prompt, pattern=None, allow_blank=False):
    while True:
        user_input = input(prompt).strip()
        if allow_blank and user_input == "":
            return user_input
        if pattern and not pattern.match(user_input):
            print("Invalid input. Please try again.")
        else:
            return user_input

def add_contact():
    unique_id = get_valid_input("Enter unique identifier (phone/email): ", re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$|^\+?[0-9]{10,15}$"))
    if unique_id in contacts:
        print("Contact already exists.")
        return

    contacts[unique_id] = {
        "Name": input("Enter name: ").strip(),
        "Phone": get_valid_input("Enter phone: ", phone_pattern),
        "Email": get_valid_input("Enter email: ", email_pattern),
        "Additional Info": input("Enter additional info: ").strip()
    }
    print("Contact added.")

def edit_contact():
    unique_id = input("Enter unique identifier of contact to edit: ").strip()
    if unique_id not in contacts:
        print("Contact not found.")
        return

    print("Leave fields blank to keep current values.")
    contacts[unique_id]["Name"] = get_valid_input("Enter new name: ", allow_blank=True) or contacts[unique_id]["Name"]
    contacts[unique_id]["Phone"] = get_valid_input("Enter new phone: ", phone_pattern, True) or contacts[unique_id]["Phone"]
    contacts[unique_id]["Email"] = get_valid_input("Enter new email: ", email_pattern, True) or contacts[unique_id]["Email"]
    contacts[unique_id]["Additional Info"] = input("Enter new additional info: ").strip() or contacts[unique_id]["Additional Info"]
    print("Contact updated.")

def delete_contact():
    unique_id = input("Enter unique identifier of contact to delete: ").strip()
    if contacts.pop(unique_id, None):
        print("Contact deleted.")
    else:
        print("Contact not found.")

def search_contact():
    unique_id = input("Enter unique identifier to search: ").strip()
    contact = contacts.get(unique_id)
    if contact:
        for key, value in contact.items():
            print(f"{key}: {value}")
    else:
        print("Contact not found.")

def display_all_contacts():
    if contacts:
        for unique_id, details in contacts.items():
            print(f"\nIdentifier: {unique_id}")
            for key, value in details.items():
                print(f"{key}: {value}")
    else:
        print("No contacts available.")

def export_contacts(filename="contacts.txt"):
    try:
        with open(filename, "w") as file:
            for unique_id, details in contacts.items():
                file.write(f"Identifier: {unique_id}\n")
                for key, value in details.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")
        print("Contacts exported.")
    except Exception as e:
        print(f"Error exporting contacts: {e}")

def import_contacts(filename="contacts.txt"):
    if not os.path.exists(filename):
        print("File not found.")
        return
    try:
        with open(filename, "r") as file:
            data = file.read().strip().split("\n\n")
            for block in data:
                lines = block.split("\n")
                unique_id = lines[0].split(": ")[1]
                contacts[unique_id] = {
                    "Name": lines[1].split(": ")[1],
                    "Phone": lines[2].split(": ")[1],
                    "Email": lines[3].split(": ")[1],
                    "Additional Info": lines[4].split(": ")[1]
                }
        print("Contacts imported.")
    except Exception as e:
        print(f"Error importing contacts: {e}")

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")


def main():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-8): ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Exiting.")
            break
        else:
            print("Invalid option. Please choose 1-8.")

if __name__ == "__main__":
    main()
