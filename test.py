#name = input("what is your name? ")
#color = input("what color you like " +name + " ")
#dob = input("what's you year of birth" )
#age = 2019 - int(dob)
#print("I am " + name + " I like " + color)
#print(age)

#help(list.sort)
#course=["Python for Beginners","Abfnska"]
#print(course.find("e"))
#course.sort()
#print(course)


#x=2.9
#print(abs(0))


#first='Gowtham'
#last='Arul'
#message= first + '[' + last + '] is learning python'
#msg=f'{first} [{last} ] is learning python'
#print(msg)

#####################  Guessing Game  #######################

# guess_no=5
# guess_count=0
# guess_limit=3
# while guess_count < guess_limit :
#    guess=int(input("guess the number: "))
#    guess_count += 1
#    if guess_no == guess :
#        print("yep, Correct")
#        break
# else:
#    print("Better Luck Next Time")
# print("Bye")

######################    Car Game  #####################


#car=""
#started = False
#while car != "quit":
#    car=input("> ").lower()
#    if car == "help":
#        print("""
#        start - to start the car
#        stop - to stop the car
#        quit - to exit the car
#        """)
#    elif car == "start":
#        if started:
#            print("car has already started")
#        else:
#            started = True
#            print("Car has been strated")
#    elif car == "stop":
#        if not started:
#            print("Car has already stopped")
#        else:
#            started= False
#            print("car has been stopped")
#    elif car == "quit":
#        print("Game Over")
#        break
#    else:
#        print("please enter the right info......:-("( ))

#################################  Banking Method  ###############

#price=[10,20,40]
#total=0
#for i in price:
#    total += i
#    print(f"Total is : {total}")   ##### we can use this for transaction details
#print(f"Total amnt is : {total}")

#########################   nested loop  ###################

#i=[9,3,5,2,7,1]
#for x in i:
#    output=""
#    for y in range(x):
#        output += "X"
#    print(output)

############################### Difference in the squence  ##################################

#num=[3,2,1,6,9,4]
#max=num[0]
#min=num[0]
#for i in num:
#    if i > max :
#        max= i
#print(f"max is : {max}")
#for j in num:
#    if j < min :
#        min=j
#print(f"min is : {min}")
#x=max-min
#print(f"difference is: {x}")

###########################    Matrix  ########################################

#matrix= [
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
#]

#print(matrix[2][2])

#no=[1,3,5,2,3]
#print(no.count(3))


###########################   Removing duplicate number from the queue  & print in acsending #########################


#num=[1,2,4,5,3,6,3,4,6,2,1,8,0,9,7,6,4]
#uniq=[]
#print(num)
#for nums in num:
#    if nums not in uniq:
#        uniq.append(nums)
#        uniq.sort()
#print(uniq)

##########################################################################################################

#cust= {
#    "name": "AG",
#    "age": 24,
#"is_verified": True
#}
#print(cust["name"])
#print(cust.get("DOB","Oct 1995"))


##############################  Number to Word using Dictionary method #####################

#phn=input("Phone :" )
#digits={
#    "1": "One",
#    "2": "Two",
#    "3": "Three",
#    "4": "Four",
#    "5": "Five"
#}
#output=""
#for ch in phn:
#    output += digits.get(ch, '"Oops"') + " "
#print(output)

#################################  Def #################################

#def greet(first_name, last_name):
#    print(f'hi {first_name} {last_name}')
#    print('Welcome to the programing world')


#print('start')
#greet('Gowtham', 'Arul')
#print('Done')

###########################  Key Word Arguments  ####################################


#def greet(first_name, last_name):
#    print(f'hi {first_name} {last_name}')
#    print('Welcome to the programing world')


#print('start')
#greet('Gowtham', last_name='Arul')  #-> keyword arguments
#print('Done')

##############################  Returing a value ################################

#def square(num):
#    return num*num


#result=square(5)
#print(result)
    #or
#print(square(6))

             ##############  OR  #####################

#def square(num):
#    print(num*num)


#square(3)

#########################   Exception Handling ##################

#try:
#    age=int(input('age: '))
#    income=20000
#    risk= income / age
#    print('age = ', age)
#    print('risk = ', risk)
#except ValueError:
#    print('Invalid Value')
#except ZeroDivisionError:
#    print('Value should not be zero')

####################    Class  #############################

#class Point:
#    def __init__(self, x, y):
#        self.x=x
#        self.y=y

#    def move(self):
#        print('move')

#    def draw(self):
#        print('draw')

#point1=Point(10, 20)   #####   Calling the class (Point) using the object called point1
#point1.x=30
#print(point1.x)


#########################  Kadane's Algorithm  ###########################################

# def max_sum_subarray(arr):
#     size = len(arr)
#     curr_sum = 0
#     max_so_far = arr[0]
#     st = 0
#     end = 0
#     poi = 0
#     for i in range(0,size):
#         curr_sum = curr_sum + arr[i]
#         if (max_so_far < curr_sum):
#             max_so_far = curr_sum
#             st = poi
#             end =i
#         if (curr_sum < 0):
#             curr_sum = 0
#             poi = i+1
5


#     print("Max_So_Far : ", max_so_far)
#     print("start : ", st)
#     print("end : ", end)

# arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
# max_sum_subarray(arr)

############################################################################