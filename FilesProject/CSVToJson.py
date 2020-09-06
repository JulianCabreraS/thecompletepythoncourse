file = open('csv_file.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]
new_list = list()

keys = ['club', 'city', 'country']
for line in lines:
    elements = line.split(",")
    new_list.append(dict(zip(keys, elements)))

print(new_list)

