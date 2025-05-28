# book.py:

class Book:
    def __init__(self, title, author):
        # Initialize the book object with title and author
        self.title = title
        self.author = author

    def display_info(self):
        # Display the information of the book
        print(f"Book: {self.title}, Author: {self.author}")