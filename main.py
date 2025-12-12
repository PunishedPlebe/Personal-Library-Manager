from library import Library
from book_builder import Builder

def main():
    book_constructor = Builder()
    lib = Library()
    program_running = True
    while program_running:
        print("welcome to Library Manager!")
        print("==============================")
        print("Main Menu")
        print("==============================")
        print("1: Add Book(s)")
        print("2: Remove Book(s)")
        print("3: Modify Book(s)")
        print("4: Print Library")
        user_input = input("Please Select An Option: ")
        
        if user_input == "1":
            function_running = True
            while function_running:
                print("Adding Books")
                adding_title = get_title_from_user()
                adding_author = get_author_from_user()
                adding_date = get_date_from_user()
                adding_genre = get_genre_from_user()
                adding_isbn = get_isbn_from_user()
                new_book = book_constructor.build_book(adding_title, adding_author, adding_date, adding_genre, adding_isbn)
                lib.add_book(new_book)

                while True:
                    exit_input = input("Would you like to continue?(Y/N): ")
                    if exit_input == "Y" or exit_input == "yes" or exit_input == "y":
                        break
                    elif exit_input == "N" or exit_input == "no" or exit_input == "n":
                        function_running = False
                        break
                    else:
                        print("Invalid Input")
            print(lib)

                


def get_title_from_user():
    user_input = input("Please Enter Title: ")
    return user_input

def get_author_from_user():
    user_input = input("Please Enter Author: ")
    return user_input

def get_genre_from_user():
    user_input = input("Please Enter Genre: ")
    return(user_input)

def get_isbn_from_user():
    while True:
        user_input = (input("Please Enter ISBN: "))
        try:
            isbn = int(user_input)
            return isbn
        except TypeError:
            print("Invalid Input, ISBN must be an Integer")

def get_date_from_user():
    while True:
        user_input = input("Please Enter Date(MM/DD/YYYY): ")
        if len(user_input) == 10:
            month = user_input[0:2]
            day = user_input[3:5]
            year = user_input[6:]
            if month.isdigit() and user_input[2] == "/" and day.isdigit() and user_input[5] == "/" and year.isdigit():
                if (int(month) <= 12 and int(month) > 0) and (int(day) <= 31 and int(day) > 0):
                    return(user_input)
                else:
                    print("Impossible Value for Month and/or Day")
            else:
                print("Incorrect Date Formatting")
        else:
            print("Incorrect Date Formatting")

def get_read_status_from_user():
    while True:
        user_input = input("Please Enter Read Status (Y/N): ")
        if user_input == "Y" or user_input == "Yes":
            return(True)
        elif user_input == "N" or user_input == "No":
            return(False)
        else:
            print(f"{user_input} is not a vaild input")


main()