contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address (optional): ")
    address = input("Enter address (optional): ")

    contacts[name] = {
        'phone': phone,
        'email': email if email else None,
        'address': address if address else None
    }
    print(f"Contact for {name} added successfully.\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            if details['email']:
                print(f"Email: {details['email']}")
            if details['address']:
                print(f"Address: {details['address']}")
            print()

def search_contact():
    search_name = input("Enter the name of the contact to search: ")

    if search_name in contacts:
        details = contacts[search_name]
        print(f"\nFound contact for {search_name}:")
        print(f"Phone: {details['phone']}")
        if details['email']:
            print(f"Email: {details['email']}")
        if details['address']:
            print(f"Address: {details['address']}")
        print()
    else:
        print("Contact not found.\n")

def update_contact():
    name_to_update = input("Enter the name of the contact to update: ")

    if name_to_update in contacts:
        print("Updating contact details for", name_to_update)
        new_phone = input("Enter new phone number: ")
        new_email = input("Enter new email address (optional): ")
        new_address = input("Enter new address (optional): ")

        contacts[name_to_update] = {
            'phone': new_phone,
            'email': new_email if new_email else None,
            'address': new_address if new_address else None
        }
        print(f"Contact for {name_to_update} updated successfully.\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")

    if name_to_delete in contacts:
        del contacts[name_to_delete]
        print(f"Contact for {name_to_delete} deleted successfully.\n")
    else:
        print("Contact not found.\n")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
