#7-1
# prompt = input("What kind of rental car would you like?")
# print("Let me see if I can find you a "+ prompt)

#7-2
prompt = input("How many people are in your dinner group?")
prompt = int(prompt)
if prompt > 8:
    print("You will need to wait for a table.")
else:
    print("Your table is ready")