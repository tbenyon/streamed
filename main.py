import pickle

users = [
    {
        "name": "Tom",
        "password": "pw1",
        "address": "123 Monkey Road",
        "dob": "15/1/1987",
        "gender": "male",
        "interests": ["action", "Nick Cage"]
     },
    {
        "name": "Gerald",
        "password": "pw2",
        "address": "234 Elephant Road",
        "dob": "15/1/1986",
        "gender": "male",
        "interests": ["romance"]
    }
]

def save_users():
    pickle_file = open('data/users.pickle', 'wb')
    pickle.dump(users, pickle_file)
    pickle_file.close()

def load_users():
    global users
    pickle_file = open('data/users.pickle', 'rb')
    users = pickle.load(pickle_file)
    pickle_file.close()

def create_user():
    requested_user_name = input("What would you like your username to be?")
    password = input("What would you like your password to be?")
    dob = input("What is your dob? (DD/MM/YYYY)")
    gender = input("What is your gender?")
    address = input("What is your address?")

    user = {
        "name": requested_user_name,
        "password": password,
        "address": address,
        "dob": dob,
        "gender": gender,
    }

    users.append(user)

load_users()

print(users)

create_user()

print(users)

save_users()