# import json

# filename = 'fav_number.json'
# try:
#     with open(filename) as f_obj:
#         fav_number = json.load(f_obj)
# except FileNotFoundError:
#     fav_number = input("What is your favorite number?")
#     with open(filename, 'w') as f_obj:
#         json.dump(fav_number, f_obj)
#         print("We'll remember your favorite number when you come back")
# else:
#     print("I know your favorite number! It's " + fav_number)

import json

def get_stored_username():
    """ Get stored username if available """
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print("Type y for yes, n for no")
        answer = input("Is this your username ? " + username + " ")
        if answer == 'y':
            print("Welcome back, " + username)
        else if answer == 'n':
            username = get_new_username()
            print("We'll remember you when you come back, " + username )
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username )

greet_user()