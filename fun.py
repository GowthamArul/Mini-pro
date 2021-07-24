# Functions

# def hello():
#     print("Hello World")

# hello()

# =================================

# Function arguments and parameters

# def add(x, y):
#     b = x+y
#     return b
# print(add(4,7))


# def say_hello(name, surname):
#     print(f"Hello, {name} {surname}")

# say_hello(name="gowtham",surname="arul") # Keyword or named arguments

# def divide(dividend, divisor):
#     if divisor != 0:
#         return dividend/divisor
#     else:
#         retirn "Invalid values"

# result = divide(15, divisor=0)  # positional argument and keyword argument, Always keyword argument should be later (after positional arguments) or both should be keyword arguments
# print(result)

# Default parameters value

# def add(x,y=8): # x is required paramter, y is optional parameter
#     print(x+y)
# add(5)

# Lambda functions ==================================================

# Lambda's are function without a name

# def add(x,y):
#     return x + y
# print(add(5,7))

# instead we will use lambda funtion

# add = lambda x, y : x + y
# print(add(4,6))
# print((lambda x, y : x + y)(5,7))

# def double(x):
#     return x *2

# seq = [1,3,5,7]
# doubled = [double(x) for x in seq]
# # Instead we will use lanbda
# doubled = [(lambda x: x*2)(x) for x in seq]
# doubled = map(double, seq)
# doubled = list(map(lambda x: x*2, seq))


# =========================================

# Unpacking Arguments

# def multiply(*args): # *args will get all the arguments which are passed
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg
#     return total

# print(multiply(1,3,5))

# def add(x, y):
#     return x + y
# nums = {"x": 15, "y":25}
# print(add(**nums)) # **nums (Keywork argument) will get the dictionary keywork and assing with respect to the values in the function arguments


# def multiply(*args): # *args will get all the arguments which are passed
#     #print(args)
#     total = 1
#     for arg in args:
#         total = total * arg
#     return total

# def apply(*args, operator):
#     if operator == "*":
#         return multiply(*args)
#     elif operator == "+":
#         return sum(args)
#     else:
#         return "Invalid"


# print(apply(1,3,6,7, operator="*"))


# ======================================

# Unpacking Keyword arguments

# def named(**kwargs):
#     print(kwargs)

# named(name="Bob", age=25)

# def both(*args, **kwargs): # *args used to collect all positional arguments and **kwargs used to collect all keywork arguments or ** will collect the dictionary values
#     print(args)
#     print(kwargs)

# both(1,3,5, name="Bob", age=25)