from book_builder import Builder
def builder_test():
    print("Testing the Book Builder")
    print("Attempting to build book")
    test_builder = Builder()
    new_book = test_builder.build_book("The Alchemist", "Paulo Coelho", "1988", "Adventure/Philosophical", 9780061122415, False)
    print(new_book)

builder_test()