# methods : __str__ and __repr__ (magic methods)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"name: {self.name}, {self.age} year old."

#     def __repr__(self): # unambiguous (தெளிவற்ற) method, used for python debugger
#         return f"<Person({self.name}, {self.age})>"

# person = Person("Bob", 28)
# print(person)