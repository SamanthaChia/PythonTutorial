# pizzas = ['pepperoni', 'hawaiian', 'marinara']
# friend_pizzas = pizzas[:]

# pizzas.append('chicken')
# friend_pizzas.append('vegetable')

# print("My favorite pizzas are: ")
# for pizza in pizzas:
#     print(pizza)
    
# print("\nMy friend's favorite pizzas are: ")
# for friend_pizza in friend_pizzas:
#     print(friend_pizza)

# Store information about a pizza being ordered.
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }

# print("You ordered a " + pizza['crust'] + "-crust pizza with the following toppings: ")

# for topping in pizza['toppings']:
#     print("\t" + topping)

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make. """
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

