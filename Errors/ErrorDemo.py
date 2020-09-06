class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_cars(self, car):
        if not isinstance(car, Car):
            raise ValueError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `cars`')
        self.cars.append(car)


ford = Garage()
fiesta = Car('Ford', 'Fiesta')
try:
    ford.add_cars('Fiesta')
except TypeError:
    print("your car was not a car")
except ValueError:
    print('Something weird happened..')
finally:
    print(f'the garage now has {len(ford)} cars')