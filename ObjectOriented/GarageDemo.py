class Garage:

    # Dunder methods Dunder means double underscore 
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    def __str__(self):
        return f'garage with {len(self)} cars'


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(ford)




