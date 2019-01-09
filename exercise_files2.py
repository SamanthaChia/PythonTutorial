# filename = 'guest.txt'

# guest_name = input("Please enter your name : ")
# with open(filename,'w') as file_object:
#     file_object.write(guest_name)

# filename = 'guest_book.txt'

# guest_name = input("Please enter your name : ")
# with open(filename,'a') as file_object:
#     file_object.write(guest_name + "\n")
#     print("Welcome , " + guest_name)

filename = 'poll.txt'

reason = input("Please enter why you like programming : ")
with open(filename,'a') as file_object:
    file_object.write(reason + "\n")
    print("Thank you, your answer has been saved")
