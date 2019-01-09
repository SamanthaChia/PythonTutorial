while True:
    number1 = input("Input the first number :")
    if number1 == 'q':
        break
    try:
        number1 = int(number1)
    except ValueError:
        print("This is not a number!")

    number2 = input("Input the second number :")
    if number2 == 'q':
        break
    try:
        number2 = int(number2)
    except ValueError:
        print("This is not a number!")
    total = number1 + number2
    print("The total is : " + str(total))


