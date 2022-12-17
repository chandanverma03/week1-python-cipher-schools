#if statement
# age = int(input("Enter your age :"))
# if age >= 14:
#     print("You're above 14 and allowed for playing games")

#pass statement
# x = 18
# if x > 18:
#     pass #if we haven't write anything under the if statement then we use pass statement

#if - else statement
# age = int(input("Enter Your age: "))
# if age >= 18:
#     print("You are eligible for vote")
# else:
#     print("Your are not eligible for vote")
    
#exercise

# number = 12
# num = int(input("Enter any number between 1 to 15 :"))
# if num == 12:
#     print("YOU WIN !!!")
# else:
#     if num > 12:
#         print("too high")
#     else:
#         print("too low")
# if we are using if else condition under else condition then it is known as nested if else condition

#and , or operator

# name = "abc"
# age = 19
# if name == "abc" and age == 19:
#     print("condition True")
# else:
#     print("condition false")

# name = "Chandan"
# age = 19
# if name == "Chandan" or age == 20:
#     print("Condition is True")
# else:
#     print("COndition is False")

# name = input("Enter your name: ")
# print(name.center(len(name)+8,"*"))

#exercise
# a = input("Enter your name: ")
# b = int(input("Your age: "))
# if a[0] == ('a' or 'A') and b > 10:
#     print("You can watch coco movie.....")
# else:
#     print("Sorry, you can not watch coco movie.....")

#if elif else statement 
# elif condition is used if we have to check multiple conditions...

# age = int(input("Please enter your age: "))
# if age==0:
#     print("You can't watch ")
# else:
#     if 0<age<=3:
#         print("ticket price: Free")
#     elif 3<age<=10:
#         print("Ticket price: 150")
#     elif 10<age<=60:
#         print("Ticket price: 250")
#     else:
#         print("Ticket price: 200")

#in keyword
#if with in
# name = input("Enter your name: ")
# if "a" in name:
#     print("a is present in name")
# else:
#     print("a is not there in name")

#check empty or not in python 
# name = input("Enter your name: ")
# if name:
#     print(f"Your name is {name}")
# else:
#     print("Bruuu You didn't type anything")

#while loops
# i = 1
# while i<= 10:
#     print(f"{i} :=> Hello world ")
#     i += 1

#sum of Numbers program using while loop
# total = 0
# i = 1
# while i <= 10:
#     total += i
#     i += 1
# print(total)

# n = int(input("Enter any number: "))
# i = 1
# total = 0
# while i<=n:
#     total += i
#     i += 1
# print(total)

# a = input("Enter any number more than 1 digit: ")
# total = 0
# i = 0
# while i < len(a):
#     total += int(a[i])
#     i += 1
# print(total)

# name = input("Please enter your name : ")
# a = ""    #temp_var 
# i = 0
# while i < len(name):
#     if name[i] not in a:
#         a += name[i]
#         print(f"{name[i]}: {name.count(name[i])}")
#     i = i+1
    
#infinite loops
# i = 0
# while i <= 10:
#     print("Hello world")    #this is an infinite loop

# while True:               #for running infinite loops we use while True
#     print("hello world")

#boolean :  True, False

#for loops with range funtion
# for i in range(10):     #(10) means range goes to 0 to 9
#     print(f"{i}:=> hello world")

# for i in range(1, 11):  #(1,11) means range start from 1 and ends with 10
#     print("hello world")