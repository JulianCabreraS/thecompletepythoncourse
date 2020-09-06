bierce = { "day": "A period of twenty-four hours, mostly misspent",
           "positive": "Mistaken at the top of one's voice",
           "misfortune": "The kind of fortune that never misses",  }

print(bierce)

# Example of dictionaries
python = {'Champman': 'Graham',
          'Cleese': 'John',
          'Idle': 'Eric'}

print(python)

python['Gilliam'] ='Gerry'
print(python)

# Delete dictionaries
del python['Idle']
print(python)

# Validating existence of
print('Marx' in python)

print(python.keys())
