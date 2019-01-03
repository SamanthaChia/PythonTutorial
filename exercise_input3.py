#7-8
sandwich_orders = ['BLT', 'Chicken', 'Vegetables']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I am currently making a " + current_order.title() + " sandwich.")

    finished_sandwiches.append(current_order)

for finished_sandwich in finished_sandwiches:
    print("\nI have finished making the " + finished_sandwich + " sandwich.")
