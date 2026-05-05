# is_logged_in =  False # input("Are you loggen in or not:

# if True:
#     print("Ok")
# elif False:
#     print("Wrong credential.")
# else:
#     print("Please login")

# a = 8
# b = 4
# bigger = a if a > b else b
# print("Bigger is:", bigger)

# a = 33
# b = 332

# print("A") if a > b else print("=") if a == b else print("B")

# age = 20
# print("Child") if age > 13 else print("Adult") if age >18 else print("Adult")

# cars = ["BMW", "Volvo", "Ford"]
# print(cars[0])
# cars[1] = "Toyota"
# print(cars)
# for i in range(len(cars)):
#     print(cars[i])

# num = input("Enter a number: ")
# FinalNum = int(num)
# if FinalNum % 2:
#     print(FinalNum, "is an odd number.")
# else:
#     print(FinalNum, "is a even number.")

# age = input("Enter your age: ")
# finalAge = int(age)
# if finalAge >= 18:
#     print("Eligible")
# else:
#     print("Not eligible")

# num = input("Enter a number: ")
# finalNum = int(num)
# if finalNum > 0:
#     print("Positive")
# elif finalNum < 0:
#     print("Negative")
# else:
#     print("Zero")

# num = input("Enter a number: ")
# finalNum = int(num)
# if finalNum % 3 == 0 and finalNum % 5 == 0:
#     print("FizzBuzz")
# elif finalNum % 3 == 0:
#     print("Fizz")
# elif finalNum % 5 == 0:
#     print("Buzz")
# else:
#     print(finalNum)

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))

# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# elif num3 > num1 and num3 > num2:
#     print(num3)

# marks = input("Enter your marks: ")
# finalMarks = int(marks)

# if finalMarks >= 90:
#     print("A")
# elif finalMarks >= 75 and finalMarks <= 89:
#     print("B")
# elif finalMarks >= 50 and finalMarks <= 74:
#     print("C")
# else:
#     print("Fail")

# print("5" < "50")

# username = input("Enter your username: ")
# password = int(input("Enter your password: "))

# if username == "admin" and password == 1234:
#     print("Login Success")
# else:
#     print("Invalid Credentials")

# num = int(input("Enter a number: "))
# if num <= 10:
#     print("Low")
# elif num <= 50:
#     print("Medium")
# elif num <= 100:
#     print("High")
# else:
#     print("Out of range")

# num = int(input("Enter a number: "))
# if num % 2 == 0 and num > 0:
#     print("Valid")
# else:
#     print("Invalid")

# username = input("Enter your username: ").strip()
# age = int(input("Enter your age: "))
# password = input("Enter yoour password: ")

# if username == "":
#     print("Invalid Username")
# elif age < 18:
#     print("Underage")
# elif len(password) < 6:
#     print("Weak Password")
# else:
#     print("Registration Successful")


# username = input("Enter your username: ")
# password = input("Enter you password: ")

# if username == "admin" and password == "1234":
#     print("Login Success")
# elif password != "1234":
#     attempt = 2
#     for i in range(attempt):
#         password = input("Please enter correct password: ")
#         if password == "1234":
#             print("Login Success")
#             break
#         else:
#             print("Account Locked")


# attempt = 3

# for i in range(attempt):
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     if username == "admin" and password == "1234":
#         print("Login Success")
#         break
# else:
#     print("Account Locked")


# int(balance) = 10000

# balance = int(input("Enter balance: "))
# amount = int(input("Enter your withdraw amount: "))

# if balance == 100000 and amount <= balance:
#     print("Withdrawn Successfully")
# elif amount > balance:
#     print("Insufficient Balance")
# elif amount <= 0:
#     print("Invalid Amaount")

# age = input("Enter your age: ")
# finalAge = int(age)
# print(finalAge + 5)

# name = input("Enter name: ")
# city = input("Enter city: ")
# profession = input("Enter profession: ")

# print(f"Hey my name is {name}, I live in {city}, and my profession is {profession}.")

# age = input("Enter age: ")
# fAge = int(age)
# print(fAge + 5)


# marks = int(input("Enter a number: "))
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 50:
#     print("C")
# else:
#     print("Fail")

age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")
elif age < 0:
    print("Invalid Input")
else:
    print("Not eligible")