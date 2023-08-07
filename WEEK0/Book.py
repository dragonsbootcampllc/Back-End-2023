class book():
    def __init__(self,title,author,genre,NoOfPages):
        self.title=title
        self.author=author
        self.genre=genre
        self.NoOfPages=NoOfPages
    
    def __repr__(self) :
        return f"The title of the book is {self.title} ,, The author of the book is {self.author} ,, The genre of the book is {self.genre} ,, The NoOfPages of the book is {self.NoOfPages} "

title=input("Enter the title of the book\n")
author=input("Enter the author of the book\n")
genre=input("Enter the genre of the book\n")
NoOfPages=int(input("Enter the number of pages of the book\n"))

b1=book(title,author,genre,NoOfPages)
print(b1.__repr__)
print(b1)
