from book import Book

class Builder:
    def __init__(self):
        self.__next_id = 1
    
    def build_book(self, title, author, publish_date, genre, ISBN, read_status=False):
        new_book = (Book(title, author, publish_date, genre, ISBN, self.__next_id, read_status))
        self.__next_id += 1
        return new_book

    def set_id(self, id):
        if not isinstance(id, int):
            raise TypeError ("ID must be an Integer")
        self.__next_id = id