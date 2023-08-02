class Book:
    def __init__(self, title, author, genre, number_of_pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.number_of_pages = number_of_pages
        
    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Number of Pages: {self.number_of_pages}"
# Creating an object of the Book class
book1 = Book("The Alchemist", "Paulo Coelho", "Fiction", 288)
# Printing the object of the Book class
print(book1)
