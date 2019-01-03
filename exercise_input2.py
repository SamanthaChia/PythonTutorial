#7-4
prompt = "\nPlease enter pizza toppings : "
prompt += "\nEnter 'quit' to end the program."

while True:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        break
    else:
        print("I'll add " + pizza_topping + " on your pizza!")