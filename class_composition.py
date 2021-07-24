# Composition is a counter part to Inheritance (The class which contain bunch of other class in it)

class Bookshelf:
    def __init__(self, *books): # removed quantity argument and replaced with *books.
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"

# shelf = Bookshelf(300)
# print(shelf)

class Book:   #(Bookshelf): (Removing the inheritance class and super class aswell )
    def __init__(self, name): # removing quantity (argument) as it is in parent class and there is no need of parent class inheritance in Composition.
        #super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"{self.name}"

book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = Bookshelf(book, book2) # This is where we are using the main composition part by calling the two objects of class Book with the parent class(Bookshelf) abject shelf.
print(shelf)