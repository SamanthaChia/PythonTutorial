#7-8,7-9
sandwich_orders = ['blt', 'chicken', 'pastrami', 'pastrami', 'vegetables', 'pastrami']
finished_sandwiches = []
print("We ran out of Pastrami!\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:    
    current_order = sandwich_orders.pop()
    print("I am currently making a " + current_order.title() + " sandwich.")

    finished_sandwiches.append(current_order)
print("\n")
for finished_sandwich in finished_sandwiches:
    print("I have finished making the " + finished_sandwich + " sandwich.")
