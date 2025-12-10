class Book:
    def __init__(self, title, author, publish_date, genre, ISBN, read_status=False, ID=1):
        if not isinstance(title, str):
            raise TypeError("Title Value Must Be A String")
        if not isinstance(author, str):
            raise TypeError("Author Value Must Be A String")
        if not isinstance(publish_date, str):
            raise TypeError("Publish Date Value Must Be A String")
        if not isinstance(genre, str):
            raise TypeError("genre Value Must Be A String")
        if not isinstance(ISBN, int):
            raise TypeError("ISBN Value Must Be A Int")
        if not isinstance(read_status, bool):
            raise TypeError("Read Status Value Must Be A Bool")
        if not isinstance(ID, int):
            raise TypeError("ID Value Must Be A Int")
        self.__title = title
        self.__author = author
        self.__date = publish_date
        self.__genre = genre
        self.__isbn = ISBN
        self.__read_status = read_status
        self.__id = ID
    
    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError("Title Must Be Type String")
        self.__title = new_title
    
    def get_author(self):
        return self.__author

    def set_author(self, new_author):
        if not isinstance(new_author, str):
            raise TypeError("Author Must Be Type String")
        self.__author = new_author
    
    def get_publish_date(self):
        return self.__date

    def set_publish_date(self, new_date):
        if not isinstance(new_date, str):
            raise TypeError("Date Must Be Type String")
        self.__date = new_date

    def get_genre(self):
        return self.__genre

    def set_genre(self, new_genre):
        if not isinstance(new_genre, str):
            raise TypeError("Genre Must Be Type String")
        self.__genre = new_genre
    
    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, new_ISBN):
        if not isinstance(new_ISBN, int):
            raise TypeError("ISBN Must Be Type Int")
        self.__isbn = new_ISBN
    
    def get_read_status(self):
        return self.__read_status
    
    def set_read_status(self, new_flag):
        if not isinstance(new_flag, bool):
            raise TypeError("Read Status Must Be Type Bool")
        self.__read_status = new_flag
    
    def get_id(self):
        return self.__id
    
    def set_id(self, new_id):
        if not isinstance(new_id, int):
            raise TypeError("ID Must Be Type Int")
        self.__id = new_id

    def __str__(self):
        return(f"Title: {self.__title}, Author: {self.__author}, Publish Date: {self.__date}, Genre: {self.__genre}, ISBN: {self.__isbn}, Have Read?: {self.__read_status}, ID: {self.__id}")
