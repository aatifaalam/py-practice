# print(list((1, 2, 3, 'Aatif', True, 22.4,)))

# list = ['Aatif', 24, 'Bihar', 'Software Engineer', 'Kyva']
# list[0] = "Aatif Aalam"
# print(f"Hi, my name is {list[0]}, I am {list[1]} years old, I live in {list[2]}, And I am {list[3]} at {list[4]}.")

# name = "Aatif"
# print(name)
# name = "Aalam"
# print(name)

# list = [35, 7, 897, 776868, 5, 6786, 1]
# for i in range(len(list) -1, -1, -1):
#     if list[i] == 7 or list[i] == 5 or list[i] == 6786 or list[i] == 1 or list[i] == 897 or list[i] == 35 or list[i] == 776868:
#         list.pop(i)
# print(list)   

# list.sort()
# print(list[3])
# print(list)

# list =(1, 3, 4)
# print(type(list))

# movies = []
# m1 = input("Enter 1st movie name: ")
# movies.append(m1)
# m2 = input("Enter 2nd movie name: ")
# movies.append(m2)
# m3 = input("Enter 3rd movie name: ")
# movies.append(m3)
# print(movies)

# list1 = [1,2,1]
# list2 = [1,2,1]
# if list1 == list2:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# nums = [10, 20, 30, 40]
# total = 0
# for i in range(len(nums)):
#     total = total + nums[i]
# print(total)    

# nums = [5, 2, 9, 1]
# nums.sort()
# print(nums[-1])

# nums = [1,2,3,4,6]
# count_of_even_nums = 0
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         count_of_even_nums = count_of_even_nums+1
# print(count_of_even_nums)        

# nums = [1, 2, 3, 4]
# rev_nums = []
# for i in range(len(nums)):
#     rev_nums.append(nums[len(nums) - 1 - i])
# print(rev_nums)

# final_List = []
# num1 = 5
# while num1 > 0:
#     num = int(input("Enter numbers: "))
#     final_List.append(num)
#     num1 -= 1
# n1 = final_List.append(int(input("Enter n1: ")))
# n2 = final_List.append(int(input("Enter n2: ")))
# n3 = final_List.append(int(input("Enter n3: ")))
# n4 = final_List.append(int(input("Enter n4: ")))
# n5 = final_List.append(int(input("Enter n5: ")))
# print(final_List)

# nums = []
# for i in range(6):
#     num = int(input("Enter num: "))
#     nums.append(num)

# f_nums = []
# for i in range(len(nums)):
#     if i == 0 or nums[i] != nums[i - 1]:
#         f_nums.append(nums[i])
# print(f_nums)

# nums = [10, 5, 8, 20, 80]
# for i in range(len(nums)):
#     if nums[i]:
#         print(nums[i])
# nums.sort()
# print(nums[-2])

# nums = []
# for i in range(6):
#     n = int(input("Enter numbers: "))
#     nums.append(n)

# unique = []
# for n in nums:
#     if n not in unique:
#         unique.append(n)
# print(unique)        
# print(f"{len(unique)}, nums = {unique}")       

# nums = [80, 80, 80, 80, 80]
# largest = float('-inf')
# second_largest = float('-inf')
# for n in nums:
#     if n > largest:
#         largest = n
# print(largest)        
# for n in nums:
#     if n != largest and n > second_largest:
#         second_largest = n       
# print(second_largest)                

# nums = []
# for i in range(6):
#     n = int(input("Enter numbers: "))
#     nums.append(n)

# even = []
# odd = []

# for n in nums:
#     if n % 2 == 0:
#         even.append(n)
#     else:
#         odd.append(n)
# print("Even =", even)
# print("Odd =", odd)        

# nums = []
# for i in range(6):
#     n = int(input("Enter numbers: "))
#     nums.append(n)

# count_of_1 = 0
# count_of_2 = 0
# count_of_3 = 0
# for n in nums:
#     if n == 1:
#         count_of_1 = count_of_1 + 1
#     elif n == 2:
#         count_of_2 = count_of_2 + 1
#     elif n == 3:
#         count_of_3 = count_of_3 + 1

# print(count_of_1)  
# print(count_of_2)
# print(count_of_3)      

# def greet(name):
#    return name
# name = greet("Hello User")
# print(name)

# def add(a, b):
#     return a + b
# def substract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b

# Add = add(1, 2)
# print(Add)
# Substract = substract(1, 2)
# print(Substract)
# Multiply = multiply(1, 2)
# print(Multiply)

# n1 = int(input("Enter number 1: "))
# n2 = int(input("Enter number 2: "))

# def add(n1, n2):
#     return n1 + n2
# Add = add(n1, n2)
# print(Add)

# def add(a, b):
#     print(a + b)

# result = add(2, 3)
# # print(result)
# def test(x):
#     if x > 5:
#         return "A"
#     else:
#         return "B"

# print(test(10))
# print(test(3))

def func(a):
    a = a + 5
    print(a)

x = 10
func(x)
print(x)