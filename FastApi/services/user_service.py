import json

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except:
        return {}

users = load_users()

def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file)

def add_user(name, hobby):
    users[name] = hobby
    save_users()
    return users

def get_all_users():
    return users

def get_user_by_name(name):
    return users.get(name)
