# # Destructuring Variables

# people = [('Bob', 42, 'Mechanic'), ('James', 24, 'Artist'),('Harry', 32, 'Lecturer')]

# for name, age, profession in people:
#     print(f"Name: {name}, Age: {age}, Profession: {profession}")
#     # or
# for person in people:
#     print(f"Name: {person[0]}, Age: {person[1]}, Profe: {person[2]}")

# # Missing tuple value or ignoring tuple values ===============

# people1 = [('Bob', 42), ('James', 24, 'Artist'),('Harry', 32, 'Lecturer')]

# for name, age, profession in people1:
#     print(f"Name: {name}, Age: {age}, Profession: {profession}")
    
# person = ("Bob", 42, "Mechanic")
# name, _, profession = person # In this case _ will eliminate the the 2nd value in the tuple
# print(name, profession)

# head, *tail = [1,2,3,4,5,]
# print("head", head)
# print("*tail", tail)
