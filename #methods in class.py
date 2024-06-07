#methods in class
#normal method
class Book:
    total_books = 0  # class variable to keep track of total books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1  # increment total_books every time a new Book is created

    #classmethod
    def get_total_books(cls):  # class method to get total books
        return cls.total_books