from book import Book

class File_Reader:
    def __init__(self):
        pass

    def read_file(self, file_name):
        saved_book_lst = []
        try:
            with open(file_name, "r") as f:
                for line in f:
                    line.strip("\n")
                    book_info = line.split(",")
                    saved_book_lst.append(Book(book_info[0], book_info[1], book_info[2], book_info[3],int(book_info[4]),int(book_info[5]),bool(book_info[6])))
            return(saved_book_lst)
        except Exception as e:
            print(e)
