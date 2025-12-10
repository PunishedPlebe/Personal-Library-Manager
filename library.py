from book import Book

class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)
    
    def remove_book(self, book):
        unique_id = book.get_id()
        print(f"Books Unique ID is {unique_id}")
        for item in self.catalog:
            if item.get_id() == unique_id:
                self.catalog.remove(item)
                break
        print(f"{book}, does not exist inside the catalog")

    def __str__(self):
        return_string = ""
        for item in self.catalog:

