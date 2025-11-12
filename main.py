from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def view_available_books():
    for book in library_books:
        if book["available"]:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search_books(term):
    term=term.lower()
    matching_books = []
    print(f"Here are the results for the search term '{term}':")
    for book in library_books:
        if term in book["author"].lower() or term in book["genre"].lower():
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")    
            matching_books.append(book)
    print("Here is a list of all matching books:\n")
    return matching_books


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout_book(id_code):
    in_list=False
    for book in library_books:
        if book["ID"].lower()==id_code.lower():
            in_list=True
            if book["available"]==True:
                book["available"]=False
                due_date= datetime.now() + timedelta(days=14)
                book["due_date"]=due_date.strftime("%Y-%m-%d")
                book["checkouts"]+=1

                print(f"The book {book['title']} has been checked out.")
                print(f"Your book is due {book['due_date']}.")
            else:
                print(f"The book {book['title']} is already checked out.")
            break
    if in_list == False:
        print("The ID you inputted does not exist in our catalog.")





# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_book(id_code):
    in_list=False
    for book in library_books:
        if book["ID"].lower()==id_code.lower():
            in_list=True
            book["available"]=True
            book["due_date"]=None
            print(f"The book {book['title']} has been returned.")
            break
    if in_list == False:
        print("The ID you inputted does not exist in our catalog.")

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

def overdue_books():
    today=datetime.now()
    overdue_in_list=False
    print("Here is a list of all overdue books:\n")
    for book in library_books:
        if book["available"]==False and book["due_date"] is not None:
            due_date=datetime.strptime(book["due_date"], "%Y-%m-%d")
            if due_date < today:
                overdue_in_list=True
                print(f" The book {book['title']} by {book['author']} is overdue. It was due on {book['due_date']}.")
    if overdue_in_list==False:
        print("There are no overdue books in the catalog.")


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

class Book:
    def __init__(self,book_dict):
        self.id=book_dict["id"]
        self.title=book_dict["title"]
        self.author=book_dict["author"]
        self.genre=book_dict["genre"]
        self.available=book_dict["available"]
        self.due_date=book_dict["due_date"]
        self.checkouts=book_dict["checkouts"]

        def checkout(self):
            if self.available:
                self.available = False
                due_date = datetime.now() + timedelta(days=14)
                self.due_date = due_date.strftime("%Y-%m-%d")
                self.checkouts += 1
                print(f"The book {self.title} has been checked out.")
                print(f"Your book is due {self.due_date}.")
            else:
                print(f"The book {self.title} is already checked out.")

        def return_book(self):
            if not self.available:
                self.available = True
                self.due_date = None
                print(f"The book {self.title} has been returned.")
            else:
                print(f"The book {self.title} was not checked out or does not exist in our catalog.")
        
        def check_overdue(self):
            if not self.available and self.due_date:
                return datetime.strptime(self.due_date, "%Y-%m-%d") < datetime.now()
            return False

books= [Book(book) for book in library_books]

def view_available_books_class():
    for book in books:
        if book.available:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}")
def search_books_class(term):
    term=term.lower()
    matching_books = []
    print(f"Here are the results for the search term '{term}':")
    for book in books:
        if term in book.author.lower() or term in book.genre.lower():
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}")    
            matching_books.append(book)
    print("Here is a list of all matching books:\n")
    return matching_books
def checkout_book_class(id_code):
    in_list=False
    for book in books:
        if book.id.lower()==id_code.lower():
            in_list=True
            book.checkout()
            break
    if in_list == False:
        print("The ID you inputted does not exist in our catalog.")
def return_book_class(id_code):
    in_list=False
    for book in books:
        if book.id.lower()==id_code.lower():
            in_list=True
            book.return_book()
            break
    if in_list == False:
        print("The ID you inputted does not exist in our catalog.")

def overdue_books_class():
    overdue_in_list=False
    print("Here is a list of all overdue books:\n")
    for book in books:
        if book.check_overdue():
            overdue_in_list=True
            print(f" The book {book.title} by {book.author} is overdue. It was due on {book.due_date}.")
    if overdue_in_list==False:
        print("There are no overdue books in the catalog.")

def view_top_3():
    top_3_books= sorted(books, key=lambda x: x.checkouts, reverse=True)[:3]
    print("Here are the top 3 most checked-out books:\n")
    for book in top_3_books:
        print(f"Title: {book.title}, Author: {book.author}, Checkouts: {book.checkouts}")

def library_menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View Available Books")
        print("2. Search Books by Author or Genre")
        print("3. Checkout a Book by ID")
        print("4. Return a Book by ID")
        print("5. List Overdue Books")
        print("6. View Top 3 Most Checked-Out Books")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
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
    
    pass
