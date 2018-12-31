motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
# replaces honda with ducati

motorcycles.append('ducati')
print(motorcycles)
# adds ducati at the end as the last index of the list

motorcycles_insert = ['honda', 'yamaha', 'suzuki']
motorcycles_insert.insert(0, 'ducati')
print(motorcycles_insert)
# inserts ducati as index 0 and honda will become index 1

motorcycles_del = ['honda', 'yamaha', 'suzuki']
del motorcycles_del[1]
print(motorcycles_del)

motorcycles_pop1 = ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles_pop1.pop()
print("The motorcycle I owned was a " + popped_motorcycle.title() + "." )
# get the value of the popped item.

motorcycles_pop2 = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles_pop2.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# pop a value from any position and not only the lastest

motorcycles_remove = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles_remove.remove(too_expensive)
print(motorcycles_remove)
print("\nA " + too_expensive.title() + " is too expensive for me.")
# remove will only remove the first occurence of the value
# specified, if the value appears more than once in the same list
# use a loop.