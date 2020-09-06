even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}

# Decompose string in characters
print(set( 'letters' ))

drinks = { 'martini': {' vodka', 'vermouth'},
           'black russian': {' vodka', 'kahlua'},
           'white russian': {' cream', 'kahlua', 'vodka'},
           'manhattan': {' rye', 'vermouth', 'bitters'},
           'screwdriver': {' orange juice', 'vodka'}  }

for name, contents in drinks.items():
    if 'vodka' in contents:  print( name)

