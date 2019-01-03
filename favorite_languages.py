favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are: ")
    for language in languages:
        print("\t" + language.title()) 


#6-6
# take_poll = {
#     'sam': '123',
#     'test': 'value',
#     'sarah': 'c',
#     'phil': 'python',
# }

# for name in take_poll:
#     if name in favorite_languages:
#         print(name.title() + ", Thank you for responding")
#     else:
#         print(name.title() + ", please take the poll!")
        
# if 'erin' not in favorite_languages.keys():
#         print("Erin, please take our poll!\n")

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         print ("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title()+ "!")

# for name in sorted(favorite_languages.keys()):
#     print( name.title() + ", thank you for taking the poll.")

# print("\nThe following languages have been mentioned: ")
# for language in set(favorite_languages.values()):
#     print(language.title())

