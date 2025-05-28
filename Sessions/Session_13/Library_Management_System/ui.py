from library import Library

def main_menu(library):
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Books")
        print("4. Remove Book")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            title = input("Enter title to search: ")
            library.search_books(title)
        elif choice == "4":
            title = input("Enter title of book to remove: ")
            library.remove_book(title)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    my_library = Library()
    main_menu(my_library)