from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
# Define a function to view all available books
def view_available_books():
    print("Here is a list of all available books:\n")
    # Create a for loop that iterates through the library_books list
    for book in library_books:
        # Checks if the available key has a value of True, if so then it prints that book's details
        if book["available"]:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

# Define a function to search books by author or genre
def search_books(term):
    # Converts the search term to lowercase to negate any capitalization interference
    term=term.lower()
    print(f"Here are the results for the search term '{term}':")
    # Iterates through the list of library books
    for book in library_books:
        # Checks if the search term is in either the author or genre keys of the book dictionary, if so then it prints that book's details
        if term in book["author"].lower() or term in book["genre"].lower():
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")    


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

# Define a function to checkout a book by ID
def checkout_book(id_code):
    # Create a boolean variable to track if the book is found in the list
    in_list=False
    # Iterate through the list of library books
    for book in library_books:
        # Check if the book ID matches the inputted ID using .lower() to make it case-insensitive
        if book["id"].lower()==id_code.lower():
            # Set the boolean variable to True since the book is found
            in_list=True
            # Check if the book is available
            if book["available"]==True:
                # Mark the book as unavailable
                book["available"]=False
                # Set the due date to 2 weeks from now using the current time and the timedelta function
                due_date= datetime.now() + timedelta(days=14)
                # Format the due date as a string in the format YYYY-MM-DD and assign it to the book's due_date key
                book["due_date"]=due_date.strftime("%Y-%m-%d")
                # Add 1 to the book's checkout amount
                book["checkouts"]+=1
                # Print a message confirming the checkout and the due date
                print(f"The book {book['title']} has been checked out.")
                print(f"Your book is due {book['due_date']}.")
            else:
                # If the book isn't available then print a message saying it's already checked out
                print(f"The book {book['title']} is already checked out.")
            # Exit the loop since the book has been found
            break
    # If the book wasn't found in the list then print a message saying the ID doesn't exist
    if in_list == False:
        print("The ID you inputted does not exist in our catalog.")





# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# Define a function to return a book by ID
def return_book(id_code):
    # Create a boolean variable to track if the book is found in the list
    in_list=False
    # Iterate through the list of library books
    for book in library_books:
        # Check if the book ID matches the inputted ID using .lower() to make it case-insensitive
        if book["id"].lower()==id_code.lower():
            # Set the boolean variable to True since the book is found
            in_list=True
            # Mark the book as available
            book["available"]=True
            # Clear the book's due date by setting it to None
            book["due_date"]=None
            # Print a message confirming the return
            print(f"The book {book['title']} has been returned.")
            # Exit the loop since the book has been found and returned 
            break
    # If the book wasn't found in the list then print a message saying the ID doesn't exist
    if in_list == False:
        print("The ID you inputted does not exist in our catalog.")

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

# Define a function to list all overdue books
def overdue_books():
    # Get today's date and time
    today=datetime.now()
    # Create a boolean variable to track if there are any overdue books
    overdue_in_list=False
    print("Here is a list of all overdue books:\n")
    # Iterate through the list of library books
    for book in library_books:
        # Check if the book's available key is False and the due_date key is not None
        if book["available"]==False and book["due_date"] is not None:
            # Convert the due_date string to a datetime object
            due_date=datetime.strptime(book["due_date"], "%Y-%m-%d")
            # Check if the due date is less than today's date
            if due_date < today:
                # Set the boolean variable to True since there is an overdue book
                overdue_in_list=True
                # Print the book's details
                print(f" The book {book['title']} by {book['author']} is overdue. It was due on {book['due_date']}.")
    # If there are no overdue books then print a message saying so
    if overdue_in_list==False:
        print("There are no overdue books in the catalog.")


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
# Define a Book class
class Book:
    # Initialize the Book object with attributes from a book dictionary (the dictionaries in library_books)
    def __init__(self,book_dict):
        self.id=book_dict["id"]
        self.title=book_dict["title"]
        self.author=book_dict["author"]
        self.genre=book_dict["genre"]
        self.available=book_dict["available"]
        self.due_date=book_dict["due_date"]
        self.checkouts=book_dict["checkouts"]
    # Define a method to checkout the book
    def checkout(self):
        # Check if the book is available
        if self.available:
            # Mark the book as unavailable
            self.available = False
            # Set the due date to 2 weeks from now using the current date/time and the timedelta function
            due_date = datetime.now() + timedelta(days=14)
            # Format the due date as a string in the format YYYY-MM-DD and assign it to the book's due_date attribute
            self.due_date = due_date.strftime("%Y-%m-%d")
            # Increment the book's checkout count by 1
            self.checkouts += 1
            # Print a message confirming the checkout and the due date
            print(f"The book {self.title} has been checked out.")
            print(f"Your book is due {self.due_date}.")
        # If the book isn't available then print a message saying it's already checked out
        else:
            print(f"The book {self.title} is already checked out.")
    # Define a method to return the book
    def return_book(self):
        # Check if the book is not available by using the not operator to see if it isn't True
        if not self.available:
            # Mark the book as available
            self.available = True
            # Clear the book's due date by setting it to None
            self.due_date = None
            # Print a message confirming the return
            print(f"The book {self.title} has been returned.")
        # If the book is already available then print a message saying it wasn't checked out
        else:
            print(f"The book {self.title} was not checked out.")
    # Define a method to check if the book is overdue
    def check_overdue(self):
        # Check if the book is not available and has a due date by checking if it is set to False and not None
        if not self.available and self.due_date:
            # Convert the due_date string to a datetime object and check if it is less than the current date/time
            return datetime.strptime(self.due_date, "%Y-%m-%d") < datetime.now()
        # If the book is available or has no due date then return False
        return False
# Create a list of Book objects from the library_books list of dictionaries
books= [Book(book) for book in library_books]

# Define a function to view all available books
def view_available_books_class():
    print("Here is a list of all available books:\n")
    # Create a for loop that iterates through the list of Book objects
    for book in books:
        # Checks if the available attribute is True, if so then it prints that book's details
        if book.available:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}")
# Define a function to search books by author or genre
def search_books_class(term):
    # Converts the search term to lowercase to negate any capitalization
    term=term.lower()
    print(f"Here are the results for the search term '{term}':")
    # Iterates through the list of Book objects
    for book in books:
        # Checks if the search term is in either the author or genre attributes of the Book object, if so then it prints that book's details
        if term in book.author.lower() or term in book.genre.lower():
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}")   
# Define a function to checkout a book by ID 
def checkout_book_class(id_code):
    # Create a boolean variable to track if the book is found in the list
    in_list=False
    # Iterate through the list of Book objects
    for book in books:
        # Check if the book ID matches the inputted ID using .lower() to make it case-insensitive
        if book.id.lower()==id_code.lower():
            # Set the boolean variable to True since the book is found
            in_list=True
            # Call the checkout method on the Book object
            book.checkout()
            # Exit the loop since the book has been found
            break
    # If the book wasn't found in the list then print a message saying the ID doesn't exist
    if in_list == False:
        print("The ID you inputted does not exist in our catalog.")
# Define a function to return a book by ID
def return_book_class(id_code):
    # Create a boolean variable to track if the book is found in the list
    in_list=False
    # Iterate through the list of Book objects
    for book in books:
        # Check if the book ID matches the inputted ID using .lower() to make it case-insensitive
        if book.id.lower()==id_code.lower():
            # Set the boolean variable to True since the book is found
            in_list=True
            # Call the return_book method on the Book object
            book.return_book()
            # Exit the loop since the book has been found and returned
            break
    # If the book wasn't found in the list then print a message saying the ID doesn't exist
    if in_list == False:
        print("The ID you inputted does not exist in our catalog.")
# Define a function to list all overdue books
def overdue_books_class():
    # Create a boolean variable to track if there are any overdue books
    overdue_in_list=False
    print("Here is a list of all overdue books:\n")
    # Iterate through the list of Book objects
    for book in books:
        # Call the check_overdue method on the Book object, checking if it returns True
        if book.check_overdue():
            # Set the boolean variable to True since there is an overdue book
            overdue_in_list=True
            # Print the book's details
            print(f" The book {book.title} by {book.author} is overdue. It was due on {book.due_date}.")
    # If there are no overdue books then print a message saying so
    if overdue_in_list==False:
        print("There are no overdue books in the catalog.")
# Define a function to view the top 3 most checked-out books
def view_top_3():
    # Sort the list of Book objects by their checkouts attribute in descending order and get the top 3, using a lambda function as the key
    top_3_books= sorted(books, key=lambda x: x.checkouts, reverse=True)[:3]
    print("Here are the top 3 most checked-out books:\n")
    # Iterate through the top 3 books and print their details
    for book in top_3_books:
        print(f"Title: {book.title}, Author: {book.author}, Checkouts: {book.checkouts}")
# Define a function to display the library menu and handle user input
def library_menu():
    # Create an infinite loop to keep the menu running until the user chooses to exit
    while True:
        # Display the menu options
        print("\nLibrary Menu:")
        print("1. View Available Books")
        print("2. Search Books by Author or Genre")
        print("3. Checkout a Book by ID")
        print("4. Return a Book by ID")
        print("5. List Overdue Books")
        print("6. View Top 3 Most Checked-Out Books")
        print("7. Exit")
        # Get the user's choice
        choice = input("Enter your choice (1-7): ")
        # Handle the user's choice using if-elif statements
        # If choice is 1-6, call the corresponding function and get input if needed, if 7 then exit the loop, else print an error message
        if choice == '1':
            view_available_books_class()
        elif choice == '2':
            term = input("Enter an author or genre to search: ")
            search_books_class(term)
        elif choice == '3':
            id_code = input("Enter the ID of the book to checkout: ")
            checkout_book_class(id_code)
        elif choice == '4':
            id_code = input("Enter the ID of the book to return: ")
            return_book_class(id_code)
        elif choice == '5':
            overdue_books_class()
        elif choice == '6':
            view_top_3()
        elif choice == '7':
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    view_available_books()
    term_input=input("Enter in an author or genre: ")
    search_books(term_input)
    id_input=input("Enter in an ID: ")
    checkout_book(id_input)
    return_input=input("Enter in an ID to return: ")
    return_book(return_input)
    overdue_books()
    library_menu()
    
    pass
