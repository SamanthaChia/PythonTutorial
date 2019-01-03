#8-9
# magicians = ['sam', 'tom', 'tyler', 'phil', 'katie']

# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)

# show_magicians(magicians)

#8-10
magicians = ['sam', 'tom', 'tyler', 'phil', 'katie']
great_magicians =[]


def make_great(magicians,great_magicians):
    while magicians:
        current_magician = magicians.pop()
        current_magician = "The Great " + current_magician
        great_magicians.append(current_magician)

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

        

make_great(magicians[:],great_magicians)
show_magicians(magicians)
show_magicians(great_magicians)