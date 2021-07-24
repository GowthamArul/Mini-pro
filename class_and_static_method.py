# Class methods and static methods

# Syntax

# class ClassTest:
#     def instance_method(self):
#         print("This is an instance method ", self)

#     @classmethod
#     def class_method(cls): # cls will be class itself
#         print("This is a Class method ", cls)
#     @staticmethod
#     def static_method():
#         print("This is static method ")

# test = ClassTest()
# #test.instance_method()
# #test.class_method()
# test.static_method()

##########################################

# class Book:
#     types = ("hardcover", "paperback")

#     def __init__(self, name, book_type, weight):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight

#     def __repr__(self):
#         return f"<Book {self.name}, {self.book_type}, weight {self.weight}g>"

#     @classmethod
#     def hardcover(cls, name, page_weight):
#         return cls(name, cls.types[0], page_weight + 100)

# # print(Book.types) # Calling class variable
# book = Book("Harry Potter", "Comic book", 1500)
# print(book.name) # Calling from init method
# print(book) # Calling repr method
# book1 = Book.hardcover("harry potter", 1500) # Assing value to class method and calling it
# print(book1)
