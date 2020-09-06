import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file) #read file and turns it to dictionary
file.close()

print(file_contents['friends'][0])

cars = [
    {'make': "Ford", 'model':'Fiesta'},
    {'make': "Ford", 'model': 'Focus'}
]

#Go and investigate how to use json.dump
file = open('friends_json.txt', 'w')
json.dump(cars, file)
file.close()
