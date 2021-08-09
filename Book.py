class Book:
    def __init__(self,title, author):
        self.title=title
        self.author=author
    def __str__(self):
        return f"The name of the book is {self.title} and it was written by {self.author}"
class Paperbook(Book):
    def __init__(self,title,author,numPages):
        super().__init__(title,author)
        self.numPages=numPages

    def pagesGood(self,torn):
        self.numPages=self.numPages-torn
        return self.numPages
    def __str__(self):
        return f"This paperbook has {self.numPages} pages"
class EBook(Book):
    def __init__(self,title,author,size):
        super().__init__(title,author)
        self.size=size

class Library:
    def __init__(self):
        self.books=[]
    def addBooks(self,book):
        self.books.append(book)
    def __str__(self):
        return f"This library has {len(self.books)} books"

    

myPaper=Paperbook("OOP","Christoff",500)
myPaper.pagesGood(50)
print(myPaper)

myEbook= EBook("C++","Jason","3Mb")
print(myEbook)
L1=Library()
L1.addBooks(myPaper)
L1.addBooks(myEbook)
print(L1)



     
        