# write a program to demonstrate Dynamic Phonebook and Contact Directory Manager.
contacts = {}

while True:
    print("\n===== CONTACT DIRECTORY =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts[name] = {"Phone": phone, "Email": email}
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Contact Found:", contacts[name])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            field = input("Enter field to update (Phone/Email): ")
            if field in contacts[name]:
                value = input("Enter new value: ")
                contacts[name][field] = value
                print("Contact updated successfully!")
            else:
                print("Invalid field!")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        if contacts:
            print("\nContact Names:", list(contacts.keys()))
            print("Contact Details:", list(contacts.values()))
            print("\nAll Contacts:")

            for name, details in contacts.items():
                print(name, ":", details)

            # List comprehension for dynamic lookup
            phone_numbers = [details["Phone"] for details in contacts.values()]
            print("All Phone Numbers:", phone_numbers)
        else:
            print("No contacts available!")

    elif choice == "6":
        print("Exiting Contact Directory.")
        break

    else:
        print("Invalid choice! Please try again.")