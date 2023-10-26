#Implement a Library class that represents a library.
# The class should have methods to add a book, remove a book, borrow a book,
# and return a book. Each book can have attributes like title, author, and availability status.
# Implement methods to display the list of available books, borrowed books, and book details.
class Book:
    """
    """
    def __init__(self, title_val: str, author_val: str, availablity_val: bool):
        self.title: str = title_val
        self.author: str = author_val
        self.availability: bool = availablity_val

class Library():
    """
    """
    def __init__(self):
        self.book_collection: list[Book] = []
    
    def add_book(self, book_obj: Book):
        """
        """
        self.book_collection.append(book_obj)
    
    def remove_book(self, book_obj: Book):


        """
        """
        # book_collection should be updated
        self.book_collection.remove(book_obj)
    def borrow_book(self, book_title: str):
        """
        """
        # book_collection should be updated
        for book_item in self.book_collection:
            if book_title == book_item.title:
                book_item.availability = False



    
    def return_book(self, book_title: str):
        """
        """
        # book_collection should be updated

        for book_item in self.book_collection:
            if book_title == book_item.title:
                book_item.availability = True
    
    def list_of_books(self):
        """
        """
        for book_item in self.book_collection:
            print(f"Title {book_item.title}")
        # book_collection should be displayed
    
    def books_available(self):
        """
        """
        # books available should be displayed

        for book_item in self.book_collection:
            if book_item.availability == True:
                print(f"{book_item.title}")
    
    def books_details(self):
        """
        """
        # book details should be displayed
        for book_item in self.book_collection:
            print(f"Title {book_item.title}, Author {book_item.author}, Availability: {book_item.availability}")

    



if __name__ == "__main__":

    book_abc: Book = Book("ABC", "John", True) #["hello"]
    book_def: Book = Book("DEF", "Wright", True)#["hello"]
    book_ghi: Book = Book("GHI", "Jason", False)
    book_jkl: Book = Book("JKL", "Smith", True)

    library_obj: Library = Library()
    library_obj.add_book(book_abc)
    library_obj.add_book(book_def)
    library_obj.add_book(book_ghi)
    library_obj.add_book(book_jkl)

    library_obj.borrow_book("ABC")
    library_obj.books_available()





    # create object for Library

    # create few book object

    # add books to library

    # remove a book from library

    # borrow a book from library

    # return a book to library

    # list of books

    # list of available books

    # book details


