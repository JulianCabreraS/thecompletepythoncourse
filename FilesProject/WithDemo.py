import json

with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file)  # read file and turns it to dictionary
