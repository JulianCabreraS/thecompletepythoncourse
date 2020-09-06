friends = ["Rolf", "Jen", "Anne"]

# Some kind of for each
for friend in friends:
    print(friend)

elements = [0,1,2,3,4,5,6,7,8]

for _ in elements:
    print("hello world")

for index in range(5,10):
    print(index)

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 90},
]

for student in students:
    print(student["name"])