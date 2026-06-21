print("\nWelcome to the Module Tracker")
print("This program tracks the modules you have taken.")

while True:
    print("\n\n Choose the following options to get started :")
    print("\n\t Option 1 : Use the module tracker (Type 1)")
    print("\n\t Option 2 : Quit (Type 2)")
    
    choice = input("\n\tEnter choice  :")
    
    if choice == "1":
        modules = []
        number_of_modules = int(input("\nGreat! , how modules do you have ?  :"))
        print("Ok ! , list me the module that you have taken")
        
        for number_of_module in range(number_of_modules):
            name_of_modules = input("\nEnter Module : ").strip().title()
            modules.append(name_of_modules)
        
        number = len(modules)
        modules.sort()
        
        print("\nYour Modules")
        
        for i, module in enumerate(modules, start=1):

            print(f"{i}. {module}")
            
        print(f"\nTotal modules : {number}")
        
        print("\n1. Restart the program")
        print("2. Exit")
            
        restart_choice = input("Select option: ")
            
        if restart_choice == '1':
            print("Restarting...\n")
            continue
        elif restart_choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, restarting...\n")
            continue
            
    elif choice == "2":
        break
    
    else:
        print("Invalid choice! Please enter 1 or 2")