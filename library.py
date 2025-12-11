from book import Book

class Library:
    def __init__(self):
        self.__catalog = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("only Book Objects can be added to the library")
        self.catalog.append(book)
    
    def remove_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Books can be removed from the library")
        unique_id = book.get_id()
        for item in self.__catalog:
            if item.get_id() == unique_id:
                self.__catalog.remove(item)
                break
        else:
            print(f"{book}, does not exist inside the catalog")
    
    

    def __str__(self):
        holder = []
        for item in self.__catalog:
            holder.append(f"{item.get_title()}, {item.get_author()}, {item.get_publish_date()}, {item.get_genre()}, {item.get_isbn()}, {item.get_read_status()}, {item.get_id()}")
        return "\n".join(holder)
