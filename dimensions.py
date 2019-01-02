#difference between this and others is that this one is using parentheses isntead of square.
dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

#by redefining the whole tuple, you can change its value.
dimensions = (400,100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)

# will not work
# dimensions[0] = 250
# print(dimensions[0])
