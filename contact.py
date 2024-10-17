# Contact Management System

contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    store_name = input("Enter store name: ")
    address = input("Enter address: ")

    contacts[name] = {
        'Phone': phone,
        'Email': email,
        'Store Name': store_name,
        'Address': address
    }
    print(f"Contact for {name} added successfully.\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\nList of contacts:")
        for name, info in contacts.items():
            print(f"\nName: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nStore Name: {info['Store Name']}\nAddress: {info['Address']}\n")

# Function to search a contact by name or phone
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if search_term == name or search_term == info['Phone']:
            print(f"\nContact Found:\nName: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nStore Name: {info['Store Name']}\nAddress: {info['Address']}\n")
            found = True
            break
    if not found:
        print(f"No contact found with the term: {search_term}\n")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("What would you like to update?")
        print("1. Phone\n2. Email\n3. Store Name\n4. Address")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            new_phone = input("Enter new phone number: ")
            contacts[name]['Phone'] = new_phone
            print(f"Phone updated for {name}.\n")
        elif choice == '2':
            new_email = input("Enter new email address: ")
            contacts[name]['Email'] = new_email
            print(f"Email updated for {name}.\n")
        elif choice == '3':
            new_store_name = input("Enter new store name: ")
            contacts[name]['Store Name'] = new_store_name
            print(f"Store name updated for {name}.\n")
        elif choice == '4':
            new_address = input("Enter new address: ")
            contacts[name]['Address'] = new_address
            print(f"Address updated for {name}.\n")
        else:
            print("Invalid choice.\n")
    else:
        print(f"No contact found with the name {name}.\n")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.\n")
    else:
        print(f"No contact found with the name {name}.\n")

# Main menu function
def menu():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()
