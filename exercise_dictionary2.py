#6-5
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'sepik': 'new guinea',
    }

for river,country in rivers.items():
    print("The " + river.title() + " runs through " + country.title())
print("\n")
for river in rivers.keys():
    print(river)
print("\n")
for country in rivers.values():
    print(country)