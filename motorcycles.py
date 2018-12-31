# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)
# replaces honda with ducati

# motorcycles.append('ducati')
# print(motorcycles)
# adds ducati at the end as the last index of the list

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')
# print(motorcycles)
#inserts ducati as index 0 and honda will become index 1

# motorcycles = ['honda', 'yamaha', 'suzuki']
# del motorcycles[1]
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']

# popped_motorcycle = motorcycles.pop()
# print("The motorcycle I owned was a " + popped_motorcycle.title() + "." )
# get the value of the popped item.

# motorcycles = ['honda', 'yamaha', 'suzuki']
# first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# pop a value from any position and not only the lastest

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nA " + too_expensive.title() + " is too expensive for me.")
# remove will only remove the first occurence of the value
# specified, if the value appears more than once in the same list
# use a loop.