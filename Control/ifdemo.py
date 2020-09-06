friend = "rolf"
user_name = input("enter your name: ")

#if demo
if user_name == friend:
    print("hello friends")
    print("this run too.")

print("this runs anyway")

friends = ["rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]
user_name = input("Enter your name: ")

# Example of elseif
if user_name in friends:
    print("Hello, Friend!")
elif user_name in family:
    print("Hello, family")
else:
    print("I dont know you ")