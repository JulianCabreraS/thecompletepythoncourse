
friends = ["Rolf", "john", "Anna"]

counter = 0
for friend in friends:
    print(counter)
    print(friend)
    counter = counter+1

#--------- Enumerate
for counter, friend in enumerate(friends):
    print(counter)
    print(friend)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))




