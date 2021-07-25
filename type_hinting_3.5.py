# Type Hinting is new feature in python 3.5
# In in the below function (list) is a hint and return the float
# Can import Tuple, set, etc....

# def list_avg(sequence: list) -> float: 
#     return sum(sequence)/ len(sequence)

# list_avg(123)

# or

from typing import List
class Book:
    Types = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, Weighting {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.Types[0], page_weight + 100)

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.Types[1], page_weight + 100)
        
        
b1 = Book("Habit", "motivation", 128)
        
        