number1 = input("Input the first number :")
try:
    number1 = int(number1)
except ValueError:
    print("This is not a number!")

number2 = input("Input the second number :")
try:
    number2 = int(number2)
except ValueError:
    print("This is not a number!")
total = number1 + number2
print("The total is : " + str(total))


