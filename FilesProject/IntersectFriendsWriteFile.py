# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to nearby friend.

friends = input('Enter three friend names separated by commas: ').split(',')
# ['Rolf', 'Jose', 'Charlie']

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]
people.close()

# Convert Friends to set
friends_set = set(friends)

# Convert Nearby set to set
people_nearby_set = set(people_nearby)

# OPTION 1
friends_nearby_set1 = friends_set.intersection(people_nearby_set)

# OPTION 2
friends_nearby_set2 = [value for value in friends if value in people_nearby]

nearby_friends_file = open('nearby_friends.txt', 'w')
for friend in friends_nearby_set1:
    print(f'{friend} is nearby! Meet up with the them')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()



