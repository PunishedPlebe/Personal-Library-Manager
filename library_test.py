from library import Library
from book import Book
import copy

def library_test():
    print("Welcome to the Library Test Module")
    print("==================================")
    print("Testing Library Constructor")
    master_test_library = Library()
    print("==================================")
    print("Testing Library add_book Method")
    test_library1 = copy.deepcopy(master_test_library)
    test_library1.add_book(Book("The Alchemist", "Paulo Coelho", "1988", "Adventure/Philosophical", 9780061122415))
    print(test_library1)
    print("==================================")
    test_library2 = copy.deepcopy(master_test_library)
    print("Testing Library remove Method")
    test_book1 = Book("The Alchemist", "Paulo Coelho", "1988", "Adventure/Philosophical", 9780061122415, False, 1)
    test_book2 = Book("The Shadow of the Wind", "Carlos Ruiz Zafón", "2001", "Mystery / Historical Fiction", 9780143034908, False, 1)
    test_book3 = Book("Project Hail Mary", "Andy Weir", "2021", "Science Fiction", 9780593135204, False, 1)
    test_library2.add_book(test_book1)
    test_library2.add_book(test_book2)
    test_library2.add_book(test_book3)
    print(test_library2)
    test_library2.remove_book(test_book1)
    print(test_library2)
    print("==================================")
    print("Testing Library Modify Method")
    test_library3 = copy.deepcopy(master_test_library)
    print("Testing Library remove Method")
    test_book4 = Book("The Alchemist", "Paulo Coelho", "1988", "Adventure/Philosophical", 9780061122415, False, 1)
    test_book5 = Book("The Shadow of the Wind", "Carlos Ruiz Zafón", "2001", "Mystery / Historical Fiction", 9780143034908, False, 1)
    test_book6 = Book("Project Hail Mary", "Andy Weir", "2021", "Science Fiction", 9780593135204, False, 1)
    test_library2.add_book(test_book4)
    test_library2.add_book(test_book5)
    test_library2.add_book(test_book6)


    

library_test()