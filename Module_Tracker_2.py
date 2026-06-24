import os

print("\nWelcome to the Module Tracker")

# ----------------------------
# LOAD DATA
# ----------------------------
def load_modules():
    modules = []

    if os.path.exists("modules.txt"):
        with open("modules.txt", "r") as file:
            for line in file:
                modules.append(line.strip())

    return modules


# ----------------------------
# SAVE DATA
# ----------------------------
def save_modules(modules):
    with open("modules.txt", "w") as file:
        for module in modules:
            file.write(module + "\n")


# ----------------------------
# VIEW MODULES
# ----------------------------
def view_modules(modules):
    if len(modules) == 0:
        print("No modules found.")
    else:
        print("\nYour Modules:")
        for i, module in enumerate(modules, start=1):
            print(f"{i}. {module}")


# ----------------------------
# ADD MODULES
# ----------------------------
def add_modules(modules):
    try:
        number = int(input("How many modules? "))

        for i in range(number):
            module = input("Enter module: ").strip().title()

            if module not in modules:
                modules.append(module)
            else:
                print("Already exists!")

    except ValueError:
        print("Please enter a number.")

    save_modules(modules)
    print("Saved!")


# ----------------------------
# MAIN PROGRAM
# ----------------------------
modules = load_modules()

while True:
    print("\n--- MENU ---")
    print("1. View modules")
    print("2. Add modules")
    print("3. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_modules(modules)

    elif choice == "2":
        add_modules(modules)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")