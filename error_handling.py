def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0!!!")
    return dividend/divisor

students = [
    {"name": "Bob", "grades": [75,90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}")
# except ZeroDivisionError as e:
#     print(e)
#     print("There are no grade yet in the list")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("Calculated")
finally:
    print("Sucess Prg")



