import pickle

users = [
    {
        "name": "Tom",
        "address": "123 Monkey Road",
        "dob": "15/1/1987",
        "gender": "male",
        "interests": ["action", "Nick Cage"]
     },
    {
        "name": "Gerald",
        "address": "234 Elephant Road",
        "dob": "15/1/1986",
        "gender": "male",
        "interests": ["romance"]
    }
]

def save_users():
    pickle_file = open('data/users.pickle', 'wb')
    pickle.dump(users, pickle_file)

save_users()
