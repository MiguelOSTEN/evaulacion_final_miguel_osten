import os

agenda = []

def add_contact(list, name, phone, email, identification, address):
    if name == '' or phone == '' or email == '' or identification == '' or address == '':
        input('All the requested information must be filled out. Press <ENTER>')
    else:
        list.append({
            'name': name,
            'phone': phone,
            'email': email,
            'identification': identification,
            'address': address
        })
        input(f'\nThe contact {name} has been successfully registered. Press <ENTER>')

def search_contact(list, name):
    found = False
    for contact in list:
        if contact['name'] == name:
            print(f'\nInformation for {name}:')
            print(f'Phone: {contact["phone"]}')
            print(f'Email: {contact["email"]}')
            print(f'Identification: {contact["identification"]}')
            print(f'Address: {contact["address"]}')
            found = True
            break
    if not found:
        print(f'\nThe contact {name} does not exist.')

def show_all_contacts(list):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nList of contacts:')
    for contact in list:
        print(f"{contact['name']}: Phone: {contact['phone']}, Email: {contact['email']}, Identification: {contact['identification']}, Address: {contact['address']}")
    input('\nPress ENTER to continue...')

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Exit")

while True:
    menu()
    option = input('\nSelect an option: ')
    
    if option == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input('Contact name: ')
        phone = input('Phone number: ')
        email = input('Email: ')
        identification = input('Identification number: ')
        address = input('Address: ')
        add_contact(agenda, name, phone, email, identification, address)
        
    elif option == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input('Enter the name of the contact to search: ')
        search_contact(agenda, name)
        input('\nPress ENTER to continue...')
        
    elif option == '3':
        show_all_contacts(agenda)
        
    elif option == '4':
        break
        
    else:
        input('Invalid option. Press <ENTER>')
