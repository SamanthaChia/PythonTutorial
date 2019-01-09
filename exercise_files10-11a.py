import json

fav_number = input("What is your favorite number?")

filename = 'fav_number.json'
with open(filename, 'w') as f_obj:
    json.dump(fav_number, f_obj)

