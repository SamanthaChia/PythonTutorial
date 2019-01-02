pizzas = ['pepperoni', 'hawaiian', 'marinara']
friend_pizzas = pizzas[:]

pizzas.append('chicken')
friend_pizzas.append('vegetable')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
    
print("\nMy friend's favorite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza)