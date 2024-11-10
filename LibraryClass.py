class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def lend_book(self, book, user):
        if book in self.books and book.is_available:
            book.is_available = False
            print(f"{user} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book, user):
        if book in self.books and not book.is_available:
            book.is_available = True
            print(f"{user} returned '{book.title}'.")
        else:
            print(f"'{book.title}' was not borrowed.")

    def list_available_books(self):
        available_books = [book.title for book in self.books if book.is_available]
        return available_books

library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)

print(library.list_available_books())  # ['1984', 'To Kill a Mockingbird']

library.lend_book(book1, "Alice")
print(library.list_available_books())  # ['To Kill a Mockingbird']

library.return_book(book1, "Alice")
print(library.list_available_books())  # ['1984', 'To Kill a Mockingbird']
