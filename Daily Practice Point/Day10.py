# nums = [1, 2, 3, 1]
# freq = set()
# def dup(nums):
#     for i in nums:
#         if i in freq:
#             return True
#         else:
#             freq.add(1)
#     return False        
# print(dup(nums))

# users = {}
# def add_user():
#     n = int(input("Enter number: "))
#     for i in range(n):
#         name = input("Enter name: ")
#         id = int(input("Enter id: "))
#         users[id] = name
#     return users

# def search_user():
#     id = int(input("Enter user id: "))
#     if id in users:
#         return users[id]
#     else:
#         return {"message":"User not found"}

# def delete_user():
#     id = int(input("Enter a user id you want to delete: "))
#     if id in users:
#         users.pop(id)
#         return {"message":"User deleted"}
#     else:
#         return {"message":"User not found"}
    
# print(add_user())
# print(search_user())
# print(delete_user())    
# print("Final user list:", users)

# users = {}

# name = input("Enter name: ")
# age = int(input("Enter age: "))

# users = {name: age}
# users = {name: age}

# print(users)
users = {"Aatif": 22}

def add_user(name, age):
    users[name] = age

add_user("Rahul", 25)
add_user("Aatif", 30)

print(users)