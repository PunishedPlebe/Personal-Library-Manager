from book import Book

class Library:
    def __init__(self):
        self.__catalog = []


    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("only Book Objects can be added to the library")
        self.__catalog.append(book)

    
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


    def modify_book(self, book, title, author, pub_date, genre, isbn, read_status):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
        if not isinstance(pub_date, str):
            raise TypeError("Date must be a string")
        if not isinstance(genre, str):
            raise TypeError("Genre must be a string")
        if not isinstance(isbn, int):
            raise TypeError("isbn must be an Int")
        if not isinstance(read_status, bool):
            raise TypeError("read status must be a bool")
        new_title = title
        new_author = author
        new_date = pub_date
        new_genre = genre
        new_isbn = isbn
        new_read_status = read_status
        target_id = book.get_id()
        copy_to_modify = None
        book_to_mod_index = 0
        for element in self.__catalog:
            if element.get_id() == target_id:
                copy_to_modify = element
                copy_to_modify.set_title(new_title)
                copy_to_modify.set_author(new_author)
                copy_to_modify.set_publish_date(new_date)
                copy_to_modify.set_genre(new_genre)
                copy_to_modify.set_isbn(new_isbn)
                copy_to_modify.set_read_status(new_read_status)
                book_to_mod_index = self.__catalog.index(element)
                del self.__catalog[book_to_mod_index]
                self.add_book(copy_to_modify)
                break
        else:
            print("The Book You Are Trying To Modify Does Not Exist In This Library")
    
    
    def search_library(self, target): #Method That loops thought all the books in the catalog and check to see if any match the target value and returns a list of book objects that match the target
        holder_lst = []
        for book in self.__catalog:
            if self.book_matches(book, target) == True:
                holder_lst.append(book)
        if len(holder_lst) > 0:
            return(holder_lst)
        else:
            print(f"{target} was not found in the library")

    def book_matches(self, book, target): # Method that takes a book object and a target input and looks to see if any of the values stored in the book attribute match that target
        if isinstance(target, str):
            if book.get_title() == target or book.get_author() == target or book.get_publish_date() == target or book.get_genre() == target:
                return True
        elif isinstance(target, bool):
            if book.get_read_status() == target:
                return True
        elif isinstance(target, int):
            if book.get_isbn() == target or book.get_id() == target:
                return True
        else:
            False

        


    def __str__(self):
        holder = []
        for item in self.__catalog:
            holder.append(f"{item.get_title()}, {item.get_author()}, {item.get_publish_date()}, {item.get_genre()}, {item.get_isbn()}, {item.get_read_status()}, {item.get_id()}")
        return "\n".join(holder)
