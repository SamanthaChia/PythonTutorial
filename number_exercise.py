# summing a million 
numbers = list(range(1,1000001))
print("Minimum number : " + str(min(numbers)))
print("Maximum number : " + str(max(numbers)))
print(sum(numbers))

# getting Odd numbers
values = list(range(1,20,3))
print(values)

# multiple of 3
for value in range (3,30,3):
    print (value)

#cubes
# for value in range(1,11):
    cubes = value**3
    print(cubes)


#cube comprehensions
cubes = [value**3 for value in range(1,11)]
print(cubes)