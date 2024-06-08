#polymorphism
#Polymorphism is one of the core concepts of object-oriented programming (OOP). 
# It refers to the ability of different objects to respond, each in their own way, to the same message (method call).
#  Polymorphism allows for the definition of a common interface and the ability to override methods in derived classes to provide specific behavior.

#Define the Base Class and Derived Classe
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        raise NotImplementedError("Subclass must implement abstract method")

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display_info(self):
        return f"E-Book: {self.title} by {self.author}, File Size: {self.file_size}MB"

class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display_info(self):
        return f"Printed Book: {self.title} by {self.author}, Pages: {self.pages}"

#Demonstrate Polymorphism
# Function to demonstrate polymorphism
def display_book_info(book):
    print(book.display_info())

# Create instances of EBook and PrintedBook
ebook = EBook("The Great Gatsby", "F. Scott Fitzgerald", 2)
printed_book = PrintedBook("To Kill a Mockingbird", "Harper Lee", 324)

# Display the book information using the same interface
display_book_info(ebook)         # Output: E-Book: The Great Gatsby by F. Scott Fitzgerald, File Size: 2MB
display_book_info(printed_book)  # Output: Printed Book: To Kill a Mockingbird by Harper Lee, Pages: 324
