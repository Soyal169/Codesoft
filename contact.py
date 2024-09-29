# Contact Book Program

contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    # Store contact details in a dictionary
    contacts[name] = {
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    print(f"Contact {name} added successfully.")

# Function to view all contacts
def view_contacts():
    if contacts:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}")
    else:
        print("No contacts found.")

# Function to search for a contact by name or phone
def search_contact():
    search_input = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if name == search_input or details['Phone'] == search_input:
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
            found = True
    if not found:
        print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        print(f"Updating details for {name}:")
        contacts[name]['Phone'] = input("Enter new phone number: ")
        contacts[name]['Email'] = input("Enter new email address: ")
        contacts[name]['Address'] = input("Enter new address: ")
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

# Function to display the menu and get user input
def menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")
    return choice

# Main loop to run the program
def main():
    while True:
        choice = menu()

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
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact book
if __name__ == "__main__":
    main()
