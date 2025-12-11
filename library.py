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
    

                
    def __str__(self):
        holder = []
        for item in self.__catalog:
            holder.append(f"{item.get_title()}, {item.get_author()}, {item.get_publish_date()}, {item.get_genre()}, {item.get_isbn()}, {item.get_read_status()}, {item.get_id()}")
        return "\n".join(holder)
