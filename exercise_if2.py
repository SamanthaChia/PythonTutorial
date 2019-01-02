#5-3, 5-4, 5-5 Alien Colors
alien_color = ['green', 'yellow', 'red']
choosen_alien_color ='green'
points = 0
if choosen_alien_color == 'green':
    points += 5
    print("You have earned 5 points!!")
    print("Current amount of points : " + str(points))
elif choosen_alien_color == 'yellow':
    points += 10
    print("You have earned 10 points!!")
    print("Current amount of points : " + str(points))
else:
    points += 15
    print("You have earned 15 points!!")
    print("Current amount of points : " + str(points))
else:
    print("Oh no, you didn't earn any points, try again?")
    print("Current amount of points : " + str(points))

#5-6 Stages of Life
age = 13
if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are an elder")

#5-7 Favorite Fruit
favorite_fruits = ['pear', 'apple', 'peach']

if 'pear' in favorite_fruits:
    print("You really like pears!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'peach' in favorite_fruits:
    print("You really like peaches!")
if 'pineapple' in favorite_fruits:
    print("You really like pineapples!")
if 'watermelon' in favorite_fruits:
    print("you really like watermelons!")