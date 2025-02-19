from utility import parse_input,add_contact,update_contact,show_all,show_phone



def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    try:
        while True:
            user_input = input("Enter a command:").strip().lower()

            command, args = parse_input(user_input)
           
            match(command):
                case "hello":
                    print("Hello, how can I help you?")                    
                case "add":
                    add_contact(args,contacts)                    
                case "change":
                    update_contact(args,contacts)
                case "phone":
                    show_phone(args,contacts)
                case "all":
                    show_all(contacts)
                case "close" | "exit":
                    print("Goodbye!")
                    break
                case "_":
                    print("Invalid command.")
            
              
        
    except Exception as err:
        print(f"Error: {err}")


    


if __name__ == "__main__":
    main()
