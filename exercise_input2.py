#7-4
# prompt = "\nEnter 'quit' to end the program."
# prompt += "\nPlease enter pizza toppings : "

# while True:
#     pizza_topping = input(prompt)
#     if pizza_topping == 'quit':
#         break
#     else:
#         print("I'll add " + pizza_topping + " on your pizza!")

#7-5
# prompt = "\nEnter 'quit' to end the program."
# prompt += "\nPlease enter your age: "

# while True:
#     age = input(prompt)
#     age = int(age)
#     if age < 3:
#         print("The cost of your ticket is $0")
#     elif age <= 12:
#         print("The cost of yout ticket is $10")
#     else:
#         print("The cost of yout ticket is $15")

#7-6
prompt = "\nEnter 'quit' to end the program."
prompt += "\nPlease enter pizza toppings : "

active = True
while active:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        active = False
    else:
        print("I'll add " + pizza_topping + " on your pizza!")