print("============================================")  # Prints the selection menu for the UMS
print("Welcome to the University Management System!")
print("============================================")
print("")
print("Are you a(n): ")
print("")
print("1) Administrator")
print("2) Lecturer")
print("3) Student")
print("4) Registrar")
print("5) Accountant")
print("")
print("Enter 6 if you wish to exit the program.")
print("")

choice = 0  # Initializes a variable named choice to receive user input
while True:  # Repeats infinitely unless a valid choice is given
    try:
        choice = int(input("Enter your choice (1/2/3/4/5/6): "))  # Gets the user's input
        if choice in [1, 2, 3, 4, 5, 6]:  # Checks if the user input is valid
            break  # Stops the while loop
        else:
            print("You need to enter a value between 1 and 6!")
            print("")
    except ValueError:  # Exception handling in case a non-integer value is inputted
        print("You need to enter a value between 1 and 6!")
        print("")

match choice:
    case 1:
        login_admin()
    case 2:
        login_lecturer()
    case 3:
        login_student()
    case 4:
        login_registar()
    case 5:
        login_accountant()
    case 6:
        exit()
