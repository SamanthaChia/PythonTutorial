#7-1
# prompt = input("What kind of rental car would you like?")
# print("Let me see if I can find you a "+ prompt)

#7-2
# prompt = input("How many people are in your dinner group?")
# prompt = int(prompt)
# if prompt > 8:
#     print("You will need to wait for a table.")
# else:
#     print("Your table is ready")

#7-3
prompt = input("Please provide me a number and I will tell you if it is a multiple of 10 or not :")
prompt = int(prompt)
if prompt % 10 == 0:
    print(str(prompt) + " is a multiple of 10")
else:
    print(str(prompt) + " is not a multiple of 10")