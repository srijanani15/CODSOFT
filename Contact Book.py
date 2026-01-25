contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for name, info in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")

def search_contact():
    key = input("Enter name or phone number to search: ")
    for name, info in contacts.items():
        if key == name or key == info["phone"]:
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter contact name to update: ")
    if name in contacts:
        contacts[name]["phone"] = input("Enter new phone: ")
        contacts[name]["email"] = input("Enter new email: ")
        contacts[name]["address"] = input("Enter new address: ")
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("\nCONTACT BOOK MENU")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please try again.")
