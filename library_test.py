from library import Library
from book import Book
import copy

def library_test():
    print("Welcome to the Library Test Module")
    print("==================================")
    print("")
    print("Testing Library Constructor")
    print("")
    master_test_library = Library()
    print("")
    print("==================================")
    print("Testing Library add_book Method")
    print("")
    test_library1 = copy.deepcopy(master_test_library)
    test_library1.add_book(Book("The Alchemist", "Paulo Coelho", "1988", "Adventure/Philosophical", 9780061122415, 1))
    print(test_library1)
    print("==================================")
    test_library2 = copy.deepcopy(master_test_library)
    print("Testing Library remove Method")
    print("")
    test_book1 = Book("The Alchemist", "Paulo Coelho", "1988", "Adventure/Philosophical", 9780061122415, 1, False)
    test_book2 = Book("The Shadow of the Wind", "Carlos Ruiz Zafón", "2001", "Mystery / Historical Fiction", 9780143034908, 2, False)
    test_book3 = Book("Project Hail Mary", "Andy Weir", "2021", "Science Fiction", 9780593135204, 3, False)
    test_library2.add_book(test_book1)
    test_library2.add_book(test_book2)
    test_library2.add_book(test_book3)
    print("Printing Library to Ensure Population")
    print(test_library2)
    print("===================================")
    print(f"Removing Book {test_book1}")
    test_library2.remove_book(test_book1)
    print(f"Printing Library to Ensure Proper Removal")
    print(test_library2)
    print("==================================")
    print("Testing Library Modify Method")
    print("")
    test_library3 = copy.deepcopy(master_test_library)
    test_book4 = Book("The Alchemist", "Paulo Coelho", "1988", "Adventure/Philosophical", 9780061122415, 1, False)
    test_book5 = Book("The Shadow of the Wind", "Carlos Ruiz Zafón", "2001", "Mystery / Historical Fiction", 9780143034908, 2, False)
    test_book6 = Book("Project Hail Mary", "Andy Weir", "2021", "Science Fiction", 9780593135204, 3, False)
    test_library3.add_book(test_book4)
    test_library3.add_book(test_book5)
    test_library3.add_book(test_book6)
    print("Printing Libarary to Ensure Population")
    print(test_library3)
    test_library3.modify_book(test_book4, "Mod Title", "Mod Author", "Mod_date", "Mod genre", 98765432110, True)
    test_library3.modify_book(test_book6, "Mod Title 2", "Mod Author 2", "Mod Date 3", "Mod Genre 2", 12345678920, True)
    print("Printing Modified Library to Ensure Proper Modification")
    print(test_library3)
    print("Attempting Bad Modifies to Test method exceptions")
    try:
        test_library3.modify_book(test_book5, 123, "Bad Mod Test Author", "Bad Mod date", "Bad Mod Genre", 5555555555555, True)
    except Exception as e:
        print(e)
    try:
        test_library3.modify_book(test_book5, "Bad Mod Test Title", 2, "Bad Mod date", "Bad Mod Genre", 5555555555555, True)
    except Exception as e:
        print(e)
    try:
        test_library3.modify_book(test_book5, "Bad Mod Test Title", "Bad Mod Test Author", 1234, "Bad Mod Genre", 5555555555555, True)
    except Exception as e:
        print(e)
    try:
        test_library3.modify_book(test_book5, "Bad Mod Test Title", "Bad Mod Test Author", "Bad Mod date", 123, 5555555555555, True)
    except Exception as e:
        print(e)
    try:
        test_library3.modify_book(test_book5, "Bad Mod Test Title", "Bad Mod Test Author", "Bad Mod date", "Bad Mod Genre", "5555555555555", True)
    except Exception as e:
        print(e)
    try:
        test_library3.modify_book(test_book5, "Bad Mod Test Title", "Bad Mod Test Author", "Bad Mod date", "Bad Mod Genre", 5555555555555, "True")
    except Exception as e:
        print(e)


    print("==================================")
    print("Testing Library Search Method")
    print("")
    test_library4 = copy.deepcopy(master_test_library)
    test_book7 = Book("The Alchemist", "Paulo Coelho", "1988", "Adventure/Philosophical", 9780061122415, 1, False)
    test_book8 = Book("The Shadow of the Wind", "Carlos Ruiz Zafón", "2001", "Mystery / Historical Fiction", 9780143034908, 2, False)
    test_book9 = Book("Project Hail Mary", "Andy Weir", "2021", "Science Fiction", 9780593135204, 3, False)
    test_library4.add_book(test_book7)
    test_library4.add_book(test_book8)
    test_library4.add_book(test_book9)
    print("Title Search")
    print(test_library4.search_library("The Alchemist")[0])
    print("Author Search")
    print(test_library4.search_library("Andy Weir")[0])
    print("Date Search")
    print(test_library4.search_library("2001")[0])
    print("Genre Search")
    print(test_library4.search_library("Adventure/Philosophical")[0])
    print("ISBN Search")
    print(test_library4.search_library(9780061122415)[0])
    print("Read Status Search")
    print(test_library4.search_library(False))
    print("")
    print("Testing Bad Search")
    print(test_library4.search_library("Some bs that isn't actually in there"))
    print("===================================")
    #I need to add more robust testing for my library functions i'm only really taking the good path rn and i need to try and break them


    

library_test()