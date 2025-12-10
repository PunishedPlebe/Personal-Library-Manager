class Book:
    def __init__(self, title, author, publish_date, genre, ISBN, read_status=False, ID):
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
        self.__title = new_title
    
    def get_author(self):
        return self.__author

    def set_author(self, new_author):
        self.__author = new_author
    
    def get_publish_date(self):
        return self.__date

    def set_publish_date(self, new_date):
        self.__date = new_date

    def get_genre(self):
        return self.__genre

    def set_genre(self, new_genre):
        self.__genre = new_genre
    
    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, new_ISBN):
        self.__isbn = new_ISBN
    
    def get_read_status(self):
        return self.__read_status
    
    def set_read_status(self, new_flag):
        self.__read_status = new_flag
    
    def get_id(self):
        return self.__id
    
    def set_id(self, new_id):
        self.__id = new_id
