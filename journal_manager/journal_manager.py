while True:
    
    print("Welcome to your Journal Manager!")
    print("1. List the entries.")
    print("2. Create a new entry.")
    print("3. View a specific entry.")
    print("4. Delete entry.")
    print("5. Exit the program.")

    selected_command = input("What would you like to do?: ")

    print(f"You have selected {selected_command}")

    if selected_command == "1":
        print("-------------------------------------------")
        with open("journal.txt", "r") as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                print(f"{index + 1}. {line.strip()}")
        print("-------------------------------------------")

    elif selected_command == "2":
        new_entry = input("Enter the text for your new entry: ")
        # create and write to the file
        with open("journal.txt", "a") as file:
            file.write(new_entry + "\n")
    elif selected_command == "3":
        entry_to_view = int(input("Enter the number of the entry you want to view: "))
        with open("journal.txt", "r") as file:
            lines = file.readlines()
            print("\n" + lines[entry_to_view - 1])

    elif selected_command == "4":
        entry_to_delete = int(input("Enter the number of the entry you want to delete: "))
        with open("journal.txt", "r") as file:
            lines = file.readlines()
            del lines[entry_to_delete - 1]
        with open("journal.txt", "w") as file:
            file.writelines(line)

    elif selected_command == "5":
        print("Thank you for using Journal Manager")
        break
    else:
        print("Please enter a valid command.")
