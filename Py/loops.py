
# Loops

## (While) Infinite loop until the loop met with the condition

# number = 7

# while True: # (user_input != 'n':)
#     user_input = input("Would you like to play? (Y/n) ")

#     if user_input =='n':
#         break
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1: #abs is an absolute value
#         print("You were off by one")
#     else:
#         print("Sorry, it's wrong!")

# for loop #

# frineds = ["Rolf", "Jen", "Bob", "Anne"]
# for i in frineds:
#     print(f"{i} is my frnd")
    
# grades = [35, 67, 98, 100, 100]
# total = 0
# amount = len(grades)
# for i in grades:
#     total += i
# print("the average is", total/amount)

## or ##

# grades = [35, 67, 98, 100, 100]
# total = sum(grades)
# amount = len(grades)
# print(total/amount)

# another types to user using for loop

# friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# starts_s = [friend for friend in friends if friend.startswith("S")]
# s = []
# for friend in friends:
#     if friend.startswith("S"):
#         s.append(friend)
# print(starts_s)
# print(s)
