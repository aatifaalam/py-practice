# i = 0
# while (i <= 6):
#     i += 1
#     if i == 3 or i == 4 or i == 7:
#         continue
#     print(i)

# sum = 0
# for i in range(1, 11):
#     sum = sum + i
# print(sum)

# num = int(input("Enter number: "))
# for i in range(1, 11):
#     print(num, "*", i, "=", num * i) 

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# for i in range(1, 11):
    # if i == 1:
    #    print(10)
    # elif i == 2:
    #     print(9)
    # elif i == 3:
    #     print(8)
    # elif i == 4:
    #     print(7)
    # elif i == 5:
    #     print(6)
    # elif i == 6:
    #     print(5)
    # elif i == 7:
    #     print(4)
    # elif i == 8:
    #     print(3)
    # elif i == 9:
    #     print(2)
    # elif i == 10:
    #     print(1)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(1, 6):
#     for j in range(1):
#         print("*" * i)

# num = input("Enter number: ")
# print(len(num))

# num = int(input("Enter number: "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10
# print(sum)        

# x = int(input("Enter number: "))        
# while x > 0:
#     remainder = x % 10
#     print(remainder, end="")
#     x = x // 10

# for i in range(9):
#     print(i * "*")

#  Print sum of a digit

# x = int(input("Enter number: "))
# digit = 0
# while x > 0:
#     r = x % 10
#     digit = digit + r
#     x = x // 10
# print(digit)    

# for i in range(21):
#     if i % 3 == 0:
#         continue
#     print(i)

# n = int(input("Enter n: "))
# for i in range(n + 1):
#     print(i * 2)

# n = int(input("Enter n: "))
# a = 0
# for i in range(1, n+1):
#     a = a + i
#     print(a)

# n = int(input("Enter n: "))
# a = 0
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()    

# n = int(input("Enter n: "))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()

# n = int(input("Enter n: "))
# for i in range(1, n+1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2*i - 1):
#         print("*", end="")
#     print()    


n = int(input("Enter n: "))
finalNum = 0
while n > 0:
    r = n % 10
    n = n // 10
    print(r, end="")

# n = int(input("Enter n: "))
# f = 1
# while n > 0:
#     r = n % 10
#     n = n // 10
#     f = f * r
# print(f)    

# n = int(input("Enter n: "))
# a = 0
# while n > 0:
#     r = n%10
#     if r % 3 == 0:
#         a = a + 1
#     n = n//10
# print(a)    

# n = int(input("Enter n: "))
# o = n
# rev = 0
# while n > 0:
#     r = n % 10
#     rev = rev * 10 + r
#     n = n // 10
# if o == r:
#     print("Palindrom")
# else:
#     print("Not palindrome")    

# n = int(input("Enter n: "))

# n = 121
# original = n
# sum = 0
# while n > 0:
#     r = n % 10
#     a = 1
#     for i in range(1, r+1):
#         a = a * i
#     sum = sum + a  
#     n //= 10
# if sum == original:
#     print("Strong")
# else:
#     print("Not Strong")