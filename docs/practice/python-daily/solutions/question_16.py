
class Book:
    """
    """
    def __init__(self, title_val: str, author_val: str, availablity_val: bool):
        self.title: str = title_val
        self.author: str = author_val
        self.availability: bool = availablity_val

class Library:
    """
    """
    def __init__(self):
        self.book_collection: list[Book] = []
    
    def add_book(self, book_obj: Book):
        """
        """
        self.book_collection.append(book_obj)
    
    def remove_book(self, book_title: str):
        """
        """
        # book_collection should be updated
    
    def borrow_book(self, book_title: str):
        """
        """
        # book_collection should be updated
    
    def return_book(self, book_title: str):
        """
        """
        # book_collection should be updated
    
    def list_of_books(self):
        """
        """
        for book_item in self.book_collection:
            print(f"Title {book_item.title}, Author {book_item.author}, Availability: {book_item.availability}")
        # book_collection should be displayed
    
    def books_available(self):
        """
        """
        # books available should be displayed
    
    def books_details(self, book_title: str):
        """
        """
        # book details should be displayed
    



if __name__ == "__main__":

    book_abc: Book = Book("ABC", "John", True) #["hello"]
    book_def: Book = Book("DEF", "Wright", True) #["hello"]
    library_obj: Library = Library()
    library_obj.add_book(book_abc)
    library_obj.add_book(book_def)
    library_obj.list_of_books()




    # create object for Library

    # create few book object

    # add books to library

    # remove a book from library

    # borrow a book from library

    # return a book to library

    # list of books

    # list of available books

    # book details


