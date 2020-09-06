# Open the file
my_file = open('data.txt', 'r')

# Read the file
file_content = my_file.read()

# Close the file
my_file.close()
print(file_content)


# Input the name
name = input('Enter your name: ')

# Open the file
my_file = open('data.txt', 'w')
my_file.write(name)
my_file.close()
