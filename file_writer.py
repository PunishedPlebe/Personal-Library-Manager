from library import Library

class File_Writer:
    def __init__(self):
        pass

    def write_file(self, library):
        with open("library_catalog.txt", 'w') as f:
            for book in library.content():
                f.write(f"{book.get_title()},{book.get_author()},{book.get_publish_date()},{book.get_genre()},{book.get_isbn()},{book.get_id()},{book.get_read_status()}\n")
            

    
