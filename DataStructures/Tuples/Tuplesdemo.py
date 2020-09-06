# {} set
# () tupple
# [] list

#Examples of tuples
friends = ("Rolf", "Bob", "Anne")

#Example of set
art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")
print(art_friends)

art_friends.remove("Jen")
print(art_friends)

art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)

# Not in both = symetric difference
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

