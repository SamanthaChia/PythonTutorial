my_foods = ['pizza', 'falafel', 'carrot cake']
#copy an exisiting list
friend_foods = my_foods[:]

# Wrong 
# friend_foods = my_foods
# **Because this will point both of them to the same list.

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)
