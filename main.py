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
    error = True
    while error == True:
        requested_user_name = input("What would you like your username to be?")
        password = input("What would you like your password to be?")
        password2 = input("Please re-enter your password.")
        dob = input("What is your dob? (DD/MM/YYYY)")
        gender = input("What is your gender?")
        address = input("What is your address?")

        user = {
            "name": requested_user_name,
            "password": password,
            "password_validate": password2,
            "address": address,
            "dob": dob,
            "gender": gender,
        }

        error = validate_user_credentials(user)

    users.append(user)

def validate_user_credentials(user):
    if user["password"] != user["password_validate"]:
        print("Passwords do not match.")
        return True
    elif len(user["dob"]) != 10:
        print("Incorrect DOB format")
        return True
    else:
        return False

def login():
    login_correct = False
    while login_correct == False:
        username = input("What is your username?")
        password = input("What is your password?")

        for user in users:
            if user["name"] == username and user["password"] == password:
                login_correct = True

        if login_correct == True:
            print("You are logged in!")
        else:
            print("Your username or password are incorrect. Try again.")

login()

load_users()

print(users)

save_users()