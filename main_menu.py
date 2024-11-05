def check_courses_file():  # Checks if courses.txt exists, if no, it creates a new file
    courses_filepath = "courses.txt"
    try:
        file = open(courses_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(courses_filepath, "x")
        file.close()


def check_admin_file():  # Checks if admins.txt exists, if no, it creates a new file
    courses_filepath = "admins.txt"
    try:
        file = open(courses_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(courses_filepath, "x")

        print("")
        print("It seems like this is the first time running this program! Let's set up an admin account.")
        print("")
        print("==============")
        print("Create Account")
        print("==============")

        admin_id = ""
        while True:
            try:
                if len(admin_id) < 4:
                    admin_id = input("Username (min. 4 characters): ")
                else:
                    break
            except ValueError:
                pass

        admin_password = ""
        while True:
            try:
                if len(admin_password) < 7:
                    admin_password = input("Password (min. 7 characters): ")
                else:
                    break
            except ValueError:
                pass

        file.write(f"{admin_id},{admin_password}")

        print("Administrator account set up successfully!")
        print("")

        file.close()


def check_registrar_file():  # Checks if registrars.txt exists, if no, it creates a new file
    courses_filepath = "registrars.txt"
    try:
        file = open(courses_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(courses_filepath, "x")
        file.close()


def check_accountant_file():  # Checks if accountants.txt exists, if no, it creates a new file
    courses_filepath = "accountants.txt"
    try:
        file = open(courses_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(courses_filepath, "x")
        file.close()


def check_students_file():  # Checks if students.txt exists, if no, it creates a new file
    students_filepath = "students.txt"
    try:
        file = open(students_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(students_filepath, "x")
        file.close()


def check_lecturers_file():  # Checks if students.txt exists, if no, it creates a new file
    lecturers_filepath = "lecturers.txt"
    try:
        file = open(lecturers_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(lecturers_filepath, "x")
        file.close()


def check_modules_file():  # Checks if modules.txt exists, if no, it creates a new file
    modules_filepath = "modules.txt"
    try:
        file = open(modules_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(modules_filepath, "x")
        file.close()


def check_fees_files():  # Checks if fees.txt exists, if no, it creates a new file
    fees_filepath = "fees.txt"
    try:
        file = open(fees_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(fees_filepath, "x")
        file.close()


def check_grades_file():  # Checks if grades.txt exists, if no, it creates a new file
    grades_filepath = "grades.txt"
    try:
        file = open(grades_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(grades_filepath, "x")
        file.close()


def main_menu():
    check_students_file()
    check_fees_files()
    check_courses_file()
    check_grades_file()
    check_modules_file()
    check_lecturers_file()
    check_registrar_file()
    check_accountant_file()
    check_admin_file()

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
            login_admin()  # Login page for administrators
        case 2:
            login_lecturer()  # Login page for lecturers
        case 3:
            login_student()  # Login page for students
        case 4:
            login_registar()  # Login page for Registrar
        case 5:
            login_accountant()  # Login page for accountants
        case 6:
            exit()  # Exits the program


main_menu()
