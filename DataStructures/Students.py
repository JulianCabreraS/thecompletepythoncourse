students = {
    "Alice": ["ID0001", 26, "A"],
    "Bob": ["ID0002", 27, "B"],
    "Claire": ["ID0003", 17, "C"]
}

print(students["Claire"][0])
print(students["Claire"])

students = {"Alice": {"id": "ID0001", "age": 26, "grade":"A"},
            "Bob": {"id": "ID0002", "age": 27, "grade":"B"}
            }

print(students["Bob"]["age"])