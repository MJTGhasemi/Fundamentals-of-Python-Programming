# Import the main_menu function from the ui module
from ui import main_menu
from library import Library

def main():
    # Create a Library instance
    my_library = Library()
    
    # Start the main menu for the library system
    main_menu(my_library)

if __name__ == "__main__":
    main()