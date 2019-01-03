#6-8
dog = {
    'name': 'pugmaw',
    'owner': 'ahri'
}
cat = {
    'name': 'neeko',
    'owner': 'khazix'
}
hamster = {
    'name': 'bard',
    'owner': 'lucian'
}

#6-9
pets = []

pets.append(dog)
pets.append(cat)
pets.append(hamster)

# for pet in pets:
#     print(pet)

favorite_places = {
    'sam': 'japan',
    'amumu': 'egypt',
    'owen': 'home'
}

# for name,favorite_place in favorite_places.items():
#     print(name + "'s favorite place is : " + favorite_place)

#6-11
cities = {
    'singapore': {
        'country': 'singapore',
        'population': 500000,
        'fact': 'it is a small country'
    },
    'akihabara': {
        'country': 'japan',
        'population': 100000,
        'fact': 'it is the land of otakus'
    },
    'johor bahru': {
        'country': 'malaysia',
        'population' : 200000,
        'fact': 'it has alot of good food'
    }
}

for city_name,city_info in cities.items():
    print(city_name + " is a city in " + city_info['country'] +
     " with a population of " + str(city_info['population']) +
     " and heres one fact : " + city_info['fact'] )