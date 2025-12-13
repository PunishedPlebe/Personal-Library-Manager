from file_reader import File_Reader
from library import Library


def reader_test():
    reader = File_Reader()
    print("Printing the Library to Verify it has contents")
    print(reader.read_file("library_catalog.txt"))
    

reader_test()