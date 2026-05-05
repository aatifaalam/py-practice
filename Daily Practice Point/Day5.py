# def fun():
#     print("Hello")

# fun()    

# list = [1,2,3,4,5,6]
# list2 = [1,2,3,4,5,6,7]

# def fun(list):
#     print(len(list))

# fun(list)
# fun(list2)

# list = [1,2,3,4,5,6]
# for i in range(1, len(list) + 1):
#     print(i)

# num = int(input("Enter a number: "))

# def fun(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# fun(num)        

# n = int(input("Enter a number: "))
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(n)    

# temp = int(input("Enter temprature: "))
# celcius = 0
# def convert_temp(temp):
#     celcius = (temp - 32) * 5 / 9
#     print(celcius)

# convert_temp(temp)

# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def mul(a, b):
#     return a * b

# a = add(1, 2)
# print(a)
# b = sub(1, 2)
# print(b)
# c = mul(1, 2)
# print(c)

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# ans = is_even(2)    
# print(ans)

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact
# ans = factorial(5)
# print(ans)


# n = 5
# factorial = 1
# for i in range(1, n + 1):
#     factorial = factorial * i
# print(factorial)

# num = int(input("Enter a number: "))
# def is_prime(num):
#     if num == 2:
#         return True
#     elif num % 2 == 0:
#         return False
#     else:
#         return True
# ans = is_prime(num)
# print(ans)    

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# def max_of_three(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and a > c:
#         return b
#     elif c > a and c > b:
#         return c
# ans = max_of_three(a, b, c)
# print(ans)    

# num = int(input("Enter a number: "))
# def reverse(num):
#     rev = 0
#     while num > 0:
#         r = num % 10
#         rev = rev * 10 + r
#         num = num // 10
#     return rev
# ans = reverse(num)
# print(ans)

# num= 123
# while num > 0:
#     r = num % 10
#     num = num // 10
#     print(r, end="")

# num = int(input("Enter a number: "))
# def count_digits(num):
#     if num == 0:
#         return 1
#     count = 0
#     while num > 0:
#         num = num // 10
#         count = count + 1
#     return count    
# ans = count_digits(num)
# print(ans)

# num = int(input("Enter a number: "))
# def arm_strong(num):
#     original = num
#     sum = 0
#     while num > 0:
#         r = num % 10
#         sum = sum + r*r*r
#         num //= 10
#     return sum == original
# ans = arm_strong(num)
# print(ans)

# num = int(input("Enter a number: "))
# def arm_strong(num):
#     sum = 0
#     while num > 0:
#         r = num % 10
#         sum = sum + r
#         num //= 10
#     return sum    
# ans = arm_strong(num)
# print(ans)

# operator = input("Choose your operator from +, -, *: ")
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))

# def Add(operator, num1, num2):
#     if operator == "+":
#         return num1 + num2
# def Subtract(operator, num1, num2):  
#     if operator == "-":
#         return num1 - num2
# def Multiply(operator, num1, num2): 
#     if operator == "*":
#         return num1 * num2
    
# add = Add(operator, num1, num2)
# sub = Subtract(operator, num1, num2)
# mul = Multiply(operator, num1, num2)
# print(add)
# print(sub)
# print(mul)

# number = int(input("Enter a number: "))
# def sum_digits(number):
#     total = 0
#     while number > 0:
#         remainder = number % 10
#         total = total + remainder
#         number //= 10
#     return total
# ans = sum_digits(number)
# print(f"Sum of number's '{number}' digit is {ans}.")

def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiplication(a, b):
    return a * b

operator = input("Choose an operator from +, - and *: ")
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))

def calc(operator):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return substract(a, b)
    elif operator == "*":
        return multiplication(a, b)
    else:
        return "Invalid Operator"
    
ans = calc(operator)
print(ans)