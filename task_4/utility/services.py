def add_contact(args,contacts):
    if not len(args) == 2:
        print("Please check arguments")
        return

    name,phone = args
    contacts[name]=phone
    print(f"Contact {name} added.")

def update_contact(args,contacts):
    if not len(args) == 2:
        print("Please check arguments")
        return

    name,phone = args
    contacts[name]=phone
    print(f"Contact {name} updated.")

def show_all(contacts):    
    print("Contacts list") 
    if not len(contacts):
        print("List is empty.Please add contacts")   

    for name,phone in contacts.items():
        print(f"Name: {name.capitalize()} --- Phone number: {phone}")
    

def show_phone(args,contacts):
    if not len(args) == 1:
        print("Please check arguments")
        return

    name=args[0]
    if name in contacts.keys():
        print("Contact found")
        print(f"Name: {name.capitalize()} --- Phone number: {contacts[name]}")
    else:
        print(f"Contact {name.capitalize()} not found")

    