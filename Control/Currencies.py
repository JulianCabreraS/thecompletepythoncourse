# --- Examples of Destructuring
currencies = 0.8, 1.2

usd, eur = currencies
print(usd)

# --- Example of destructuring
friends = [("Rolf", 25), ("Anne",37), ("Charlie", 31), ("Bob", 22)]

for name, age in friends:
    print(f"{name} is {age} years old.")

# --- Example of destructuring using dictionaries
friend_age = {"Rolf":25, "Anne":37, "Charlie":31, "Bob":22}
for name in friend_age:
    print(name)

for name, age in friend_age.items():
    print(f"{name} is {age} years old")

# --- Example of break
cars = ["ok","ok","ok","ok","ok","faulty","ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping ")
        continue
    print(f"This is car {status}")

