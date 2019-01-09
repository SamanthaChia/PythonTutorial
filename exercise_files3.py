# while True:
#     number1 = input("Input the first number :")
#     if number1 == 'q':
#         break
#     try:
#         number1 = int(number1)
#     except ValueError:
#         print("This is not a number!")

#     number2 = input("Input the second number :")
#     if number2 == 'q':
#         break
#     try:
#         number2 = int(number2)
#     except ValueError:
#         print("This is not a number!")
#     total = number1 + number2
#     print("The total is : " + str(total))

catfile = 'cats.txt'
dogfile = 'dogs.txt'

try:
    with open(catfile) as cat_open:
        cat_contents = cat_open.read()
        print(cat_contents)
        print("\n")
except FileNotFoundError:
    pass

try:
    with open(dogfile) as dog_open:
        dog_contents = dog_open.read()  
        print(dog_contents)
except FileNotFoundError:
    print("The file " + dogfile + " is not found")