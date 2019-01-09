filename = 'learning_python.txt'

#Reading the entire file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

#Loop over the file object.
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#Store the contents in a list
with open(filename) as file_object:
    lines = file_object.readlines()

lines_read = ''
for line in lines:
    lines_read += line.strip()
