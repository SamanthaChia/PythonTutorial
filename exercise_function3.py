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

album1 = make_album('sam','testing album',4)
print(album1)
album2 = make_album('test', 'rock album')
print(album2)
album3 = make_album('nami', 'koi fish album')
print(album3)