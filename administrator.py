def login_admin():
    print("========================")
    print("Administrator Login Page")
    print("========================")

    admin_id = ""
    while True:
        if len(admin_id) < 4:
            admin_id = input("Username (min. 4 characters): ")
        else:
            break

    admin_password = ""
    while True:
        if len(admin_password) < 7:
            admin_password = input("Password (min. 7 characters): ")
        else:
            break

    check_admin_login(admin_id, admin_password)


def check_admin_login(user_id, user_password):
    admin_filepath = "../files/admins.txt"
    try:
        with open(admin_filepath, "r") as file:
            accounts = file.readlines()
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    for account in accounts:
        username, password = account.split(',')
        if user_id == username:
            if user_password == password:
                login_success()
        login_fail()


def login_success():
    print("")
    print("Admin login successful!")
    print("")

    admin_menu()


def login_fail():
    print("")
    print("The username/password you enter is incorrect! Would you like to:")
    print("1) Try again")
    print("2) Return to main menu")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2): "))  # Gets the user's input
            if choice in [1, 2]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 2!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 2!")
            print("")

    match choice:
        case 1:
            login_admin()
        case 2:
            main_menu()


def is_page_full(pages):
    length = len(pages)
    if len(pages[length]) < 5:
        return False
    return True


def create_new_page(pages):
    length = len(pages)
    pages[length + 1] = []


def write_to_page(pages, entry):
    length = len(pages)
    pages[length].append(entry)


def admin_menu():
    print("======================")
    print("Admin Menu")
    print("======================")
    print("1) Manage Courses")
    print("2) Manage Students")
    print("3) Manage Lecturers")
    print("4) Generate Report")
    print("5) View All Data")
    print("6) Log Out")
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
            manage_courses_menu()
        case 2:
            manage_students_menu()
        case 3:
            manage_lecturers_menu()
        case 4:
            generate_report()
        case 5:
            view_all_data()
        case 6:
            admin_logout()


def manage_courses_menu():
    print("======================")
    print("Courses Menu")
    print("======================")
    print("1) Add A Course")
    print("2) Remove A Course")
    print("3) View Courses")
    print("4) Return to previous menu")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))  # Gets the user's input
            if choice in [1, 2, 3, 4]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 4!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 4!")
            print("")

    match choice:
        case 1:
            add_course()
        case 2:
            delete_course()
        case 3:
            view_courses()
        case 4:
            admin_menu()


def add_course():
    courses_filepath = "../files/courses.txt"
    print("============")
    print("Add A Course")
    print("============")
    print("")

    try:
        with open(courses_filepath, "r") as file:
            courses = file.readlines()
            used_course_codes = []
            for course in courses:
                used_course_codes.append(course[0:5])
            course_code = ""
            while True:
                try:
                    if len(course_code) != 5 or course_code in used_course_codes:
                        if len(used_course_codes) == 0:
                            pass
                        else:
                            print(f"Last Used Course Code: {used_course_codes[len(used_course_codes)-1]}")
                        course_code = input("Course Code (5 characters and unique): ")
                    else:
                        break
                except ValueError:
                    pass

            course_name = input("Course Name: ")
            while True:
                try:
                    course_credits = int(input("Course Credits: "))
                    if course_credits < 1:
                        print("You need to enter an integer value larger than 0!")
                    else:
                        break
                except ValueError:
                    print("You need to enter an integer value!")
                    print("")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(courses_filepath, "a") as file:
            entry = f"{course_code},{course_name},{course_credits}\n"

            file.write(entry)

            print("")
            print("Course has been created successfully!")
            print("")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    manage_courses_menu()


def delete_course():
    courses_filepath = "../files/courses.txt"
    try:
        with open(courses_filepath, "r") as file:
            courses = file.readlines()
            available_course_codes = []
            for course in courses:
                available_course_codes.append(course[0:5])

        target_course_code = ""
        while True:
            try:
                if len(target_course_code) != 5 or target_course_code not in available_course_codes:
                    if target_course_code == 'exit':
                        manage_courses_menu()
                    if len(available_course_codes) == 0:
                        print("")
                        print("There are no courses yet! You need to create a course before deleting one.")
                        print("")
                        manage_courses_menu()
                    else:
                        print(f"The latest course code in use is {available_course_codes[len(available_course_codes)-1]}")
                        print("Enter 'exit' to return to previous menu.")
                        target_course_code = input("Course Code (5 characters and exists): ")
                else:
                    break
            except ValueError:
                pass

        for course in courses:
            if target_course_code == course[0:5]:
                courses.pop()

        try:
            with open(courses_filepath, "w") as file:
                file.writelines(courses)
            print(f"Course {target_course_code} was successfully deleted!")
            print("")
            manage_courses_menu()
        except FileNotFoundError:
            print("An error has occurred! The file was not found. Please contact developer.")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def view_courses():
    courses_filepath = "../files/courses.txt"
    pages = {1: []}

    try:
        with open(courses_filepath, "r") as file:
            courses = file.readlines()

            for course in courses:
                course = course.strip('\n')
                if is_page_full(pages):
                    create_new_page(pages)
                write_to_page(pages, course)

            print(f"There are {len(courses)} courses registered stored in {len(pages)} page(s).")
            print("")

            while True:
                for page in pages:
                    print(f"Page {page} (First Entry: {pages.get(page)[0][0:5]})")
                try:
                    target_page = int(input("Enter the desired page number: "))
                except ValueError:
                    pass
                if target_page > len(pages):
                    print(f"Page {target_page} does not exist!")
                else:
                    current_courses = pages.get(target_page)
                    for course in current_courses:
                        course_code = course[0:5]
                        course_name = ""


    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

manage_courses_menu()
