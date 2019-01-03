#8-6
# def city_country(city_name, country):
#     sentance = city_name + ", " + country
#     return sentance

# country1 = city_country('Santiago', 'Chile')
# country2 = city_country('Hokkaido', 'Japan')
# country3 = city_country('Sinagapore', 'Singapore')
# print(country1)
# print(country2)
# print(country3)

#8-7
def make_album(artist_name, album_title, no_of_tracks=''):
    if no_of_tracks:
        album ={'artist_name' : artist_name, 'album_title' : album_title, 'no_of_tracks' : no_of_tracks}
    else:   
        album ={'artist_name' : artist_name, 'album_title' : album_title}
    return album

while True:
    print("(Enter q to quit anytime)")
    print("Enter the album's artist and title!")
    artist_name = input("Artist Name: ")
    album_name = input("Album Name: ")
    if artist_name == 'q':
        break
    elif album_name == 'q':
        break
    else:
        print(make_album(artist_name,album_name))

    