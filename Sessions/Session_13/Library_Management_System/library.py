# library.py:

from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added book: {title}")

    def display_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books:
                book.display_info()
        else:
            print("No books in the library.")

    def search_books(self, title):
        # Search for books by title
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("Found Books:")
            for book in found_books:
                book.display_info()
        else:
            print("No books found.")

    def remove_book(self, title):
        # Remove a book by title
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed book: {title}")
                return
        print("Book not found.")