from book import Book

class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)
        #print(f"DEBUG TO VERIFY BOOK WAS ADDED TO CATALOG {self.catalog}")
    
    def remove_book(self, book):
        unique_id = book.get_id()
        for item in self.catalog:
            if item.get_id() == unique_id:
                self.catalog.remove(item)
                break
        else:
            print(f"{book}, does not exist inside the catalog")

    def __str__(self):
        holder = []
        for item in self.catalog:
            holder.append(f"{item.get_title()}, {item.get_author()}, {item.get_publish_date()}, {item.get_genre()}, {item.get_isbn()}, {item.get_read_status()}, {item.get_id()}")
        return "\n".join(holder)
