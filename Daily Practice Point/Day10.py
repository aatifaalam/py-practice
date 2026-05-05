users = {}
n = int(input("Enter numbers of users: "))
for i in range(n):
    name = input("Enter name: ")
    id = int(input("Enter id: "))
    users[name] = id

print(users)
