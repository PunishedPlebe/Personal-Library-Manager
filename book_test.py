from book import Book
import copy

def book_test():
    print("Welcome to The Book Object Test Module")
    print("======================================")
    print("Testing Book Class Constructor...")
    print("======================================")
    master_test_book = Book("The Alchemist", "Paulo Coelho", "1988", "Adventure/Philosophical", 9780061122415, 1)
    print(master_test_book)
    print("======================================")
    print("Testing Constructor Type Exceptions...")
    print("======================================")
    try:
        test_book1 = Book(987, "Test Author", "Test Date", "Test Genre", 123456789, 1, False) # attempting to trip title string exception
    except Exception as e:
        print(e)
    try:
        test_book1 = Book("Test Title", 123, "Test Date", "Test Genre", 123456789, 1, False,) # attempting to trip author string exception
    except Exception as e:
        print(e)
    try:
        test_book1 = Book("Test Title", "Test Author", 123, "Test Genre", 123456789, 1, False) # attempting to trip date string exception
    except Exception as e:
        print(e)
    try:
        test_book1 = Book("Test Title", "Test Author", "Test Date", 123, 123456789, 1, False) # attempting to trip genre string exception
    except Exception as e:
        print(e)
    try:
        test_book1 = Book("Test Title", "Test Author", "Test Date", "Test Genre", "123456789", 1, False) # attempting to trip ISBN Int exception
    except Exception as e:
        print(e)
    try:
        test_book1 = Book("Test Title", "Test Author", "Test Date", "Test Genre", 123456789, 1, "False") # attempting to trip Read Status bool exception
    except Exception as e:
        print(e)
    try:
        test_book1 = Book("test Title", "Test Author", "Test Date", "Test Genre", 123456789, "6", False,) # attempting to trip book id int exception
    except Exception as e:
        print(e)
    print("======================================")
    print("Testing Setter Type Exceptions...")
    print("======================================")
    test_book2 = copy.deepcopy(master_test_book)
    try:
       test_book2.set_title(123)
    except Exception as e:
        print(e)
    try:
       test_book2.set_author(123)
    except Exception as e:
        print(e)
    try:
       test_book2.set_publish_date(123)
    except Exception as e:
        print(e)
    try:
       test_book2.set_genre(123)
    except Exception as e:
        print(e)
    try:
       test_book2.set_isbn("123")
    except Exception as e:
        print(e)
    try:
       test_book2.set_read_status("False")
    except Exception as e:
        print(e)
    try:
       test_book2.set_id("123")
    except Exception as e:
        print(e)
    print("======================================")
    print("Testing getters method...")
    print("======================================")
    testbook_3 = copy.deepcopy(master_test_book)
    print(testbook_3.get_title())
    print(testbook_3.get_author())
    print(testbook_3.get_publish_date())
    print(testbook_3.get_genre())
    print(testbook_3.get_isbn())
    print(testbook_3.get_read_status())
    print(testbook_3.get_id())



book_test()