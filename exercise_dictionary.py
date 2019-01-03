#6-1 Person
person = {
    'first_name': 'samantha',
    'last_name': 'chia',
    'age': 20,
    'city': 'singapore'
}

print(person)

#6-2 Favorite Numbers
values = {
    'sam': [11, 10],
    'camille': [14],
    'solaire': [99, 1],
    'neeko': [0],
    'yasuo': [666],
}

for name, numbers in values.items():
    print(name + "'s favorite number(s) is/are : ")
    for number in numbers:
        print(str(number))
