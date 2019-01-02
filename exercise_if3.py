#5-8 , 5-9
# usernames = ['sam', 'kyrx', 'admin', 'user', 'amumu']

# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print("Hello " + username + ",would you like to see a status report?")
#         else:
#             print("Hello " + username + " thank you for logging in again")
# else:
#     print("We need to find some users!")

# 5-10 Checking Usernames
# current_users = ['sam', 'kyrx', 'admin', 'user', 'amumu']
# new_users = ['sam', 'test', 'leona', 'amumu', 'pyke']

# for new_user in new_users:
#     if new_user in current_users:
#         print("The username " + new_user + " is already taken! Please enter a new one")
#     else:
#         print("The username " + new_user + " is available!")

#5-11 Ordinal Numbers
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")