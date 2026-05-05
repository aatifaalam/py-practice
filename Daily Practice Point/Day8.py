# users = {}
# for i in range(3):
#     name = input("Enter name: ") 
#     age = int(input("Enter age: "))
#     users[name] = age
# print(users)
# n = input("Enter name that you want to check: ")

# def found_user(users, n):
#     return users.get(n)
#     # if n in users:
#     #     return "User found", users[n]
#     # else:
#     #     return "User not found"
        
# def show_adult(age):
#     return age >= 18
#     # if n not in users:
#     #     return "Error 404(User not found)"
#     # elif users[n] >= 18:
#     #     return "Adult"
#     # else:
#     #     return "Under age"   
   
# print(found_user(users, n))    
# print(show_adult(age))           


# Menu System

# while True:
#     print("\n1. Add User")
#     print("2. Show Users")
#     print("3. Search User")
#     print("4. Show Adults")
#     print("5. Exit")

#     choice = int(input("Enter choice: "))
#     n = 1
#     if choice == 1:
#         choice = n * 8000
#         print(choice)
#     elif choice == 2:
#         pass
#     elif choice == 3:
#         pass
#     elif choice == 4:
#         pass
#     elif choice == 5:
#         break
#     else:
#         print("Invalid choice")

# users = {}
# def add_users(users):
#     for i in range(3):
#         name = input("Enter name: ")
#         age = int(input("Enter age: "))
#         users[name] = age

# def show_user(users):
#     for name in users:
#         return name, users[name]

# def find_user(users):
#     user = input("Enter user name that you want to find: ")
#     age = users.get(user)
#     if age is None:
#         return "User Not Found"
#     else:
#         return "Age:", age

# def show_adult(users):
#     for name in users:
#         if name not in users:
#             return "(404 Error) User Not Found"
#         if users[name] >= 18:
#             return name, "->", users[name]
#         else:
#             return "Under Age"
# add_users(users)
# print(show_user(users))
# print(find_user(users))
# print(show_adult(users))      

def contain_duplicate():
    nums = [1,2,3,4]
    freq = {}
    for i in nums:
        if i in freq:
            return True
        else:
            freq[i] = 1         