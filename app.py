from contacts import ContactManager

def main():
    manager = ContactManager()
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            manager.add_contact(name, phone)
        elif choice == '2':
            contacts = manager.get_contacts()
            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
