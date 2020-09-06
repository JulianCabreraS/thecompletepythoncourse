
ages =[22,35, 27, 21, 20]

odds = [age for age in ages if age % 2 ==1]
print(odds)

# ------------ Example of List Comprehension
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guest_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guest_lower)
present_friends = {name.title() for name in present_friends}

print(present_friends)

# ------------Example of Dictionary comprehension
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3,7,15,11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))

}
print(long_timers)

# ------------Using zip
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3,7,15,11]

long_timers = dict(zip(friends, time_since_seen))
print(long_timers)

