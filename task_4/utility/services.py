def add_contact(args,contacts):
    if not len(args) == 2:
        return "Please check arguments"        

    name,phone = args
    contacts[name]=phone
    return f"Contact {name} added."

def update_contact(args,contacts):
    if not len(args) == 2:
        return "Please check arguments"

    name,phone = args
    contacts[name]=phone
    return f"Contact {name.capitalize()} updated."

def show_all(contacts):    
    if not len(contacts):
        return "List is empty.Please add contacts"   

    data_str=""
    for name,phone in contacts.items():
        data_str += f"Name: {name.capitalize()} --- Phone number: {phone}\n"
    return data_str

def show_phone(args,contacts):
    if not len(args) == 1:
        return "Please check arguments"

    name=args[0]
    if name in contacts.keys():
        return f"Name: {name.capitalize()} --- Phone number: {contacts[name]}"
    else:
        return f"Contact {name.capitalize()} not found"

    