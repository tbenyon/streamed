import pickle

films = [
    {
        "id": 0,
        "name": "Seven",
        "genre": "thriller",
        "lead_actor": "Lucy",
    },
    {
        "id": 1,
        "name": "Matrix",
        "genre": "action",
        "lead_actor": "Barry",
    },
    {
        "id": 2,
        "name": "Alien",
        "genre": "thriller",
        "lead_actor": "Barry",
    },
    {
        "id": 3,
        "name": "The Dark Knight",
        "genre": "action",
        "lead_actor": "Dave",
    },
    {
        "id": 4,
        "name": "Pulp Fiction",
        "genre": "action",
        "lead_actor": "Barry",
    },
    {
        "id": 5,
        "name": "The Usual Suspects",
        "genre": "thriller",
        "lead_actor": "Dave",
    },
    {
        "id": 6,
        "name": "Titanic",
        "genre": "romance",
        "lead_actor": "Lucy",
    },
    {
        "id": 7,
        "name": "The Notebook",
        "genre": "romance",
        "lead_actor": "Dave",
    }
]

current_user = ""

def save_users():
    pickle_file = open('data/users.pickle', 'wb')
    pickle.dump(users, pickle_file)
    pickle_file.close()

def load_users():
    global users
    try:
        pickle_file = open('data/users.pickle', 'rb')
        users = pickle.load(pickle_file)
        pickle_file.close()
    except:
        users = [
            {
                "name": "Tom",
                "password": "pw1",
                "address": "123 Monkey Road",
                "dob": "15/1/1987",
                "gender": "male",
                "interests": ["action", "Nick Cage"],
                "watched": []
            },
            {
                "name": "Gerald",
                "password": "pw2",
                "address": "234 Elephant Road",
                "dob": "15/1/1986",
                "gender": "male",
                "interests": ["romance"],
                "watched": []
            }
        ]
        save_users()
        print("Users seeded.")


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
    global current_user
    login_correct = False
    while login_correct == False:
        username = input("What is your username?")
        password = input("What is your password?")

        for user in users:
            if user["name"] == username and user["password"] == password:
                login_correct = True
                current_user = user["name"]

        if login_correct == True:
            print("You are logged in!")
        else:
            print("Your username or password are incorrect. Try again.")

def login_or_create_user():
    valid_choice = False
    while valid_choice == False:
        choice = input("Would you like to:\n  1: Login\n  2: Create User")
        if choice == "1":
            valid_choice = True
            login()
        elif choice == "2":
            valid_choice = True
            create_user()
        else:
            print("You must type one of the above options. Please try again.")

def watch_film():
    global current_user
    print("FILMS:")
    for film in films:
        print(str(film["id"]) + ": " + film["name"])

    film_choice = input("Which film would you like to watch? (Type the ID)")

    for user in users:
        if user["name"] == current_user:
            user["watched"].append(film_choice)
    
    save_users()

# login_or_create_user()
#
# print(users)
#
# save_users()
load_users()
login()
watch_film()