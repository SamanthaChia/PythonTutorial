cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print(cars)
# sort by ascending alphabet. (?)

cars_reverse_true = ['bmw', 'audi', 'toyota', 'subaru']
cars_reverse_true.sort(reverse=True)
print(cars_reverse_true)
# sort descending alphabet (?)

cars_reverse = ['bmw', 'audi', 'toyota', 'subaru']
cars_reverse.reverse()
print(cars_reverse)

len(cars)
# in the terminal , to get the length of the list.