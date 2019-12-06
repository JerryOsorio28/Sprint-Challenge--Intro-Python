# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle:
    def __init__(self, num_wheels):
        self.num_wheels = 4

    def drive(self):
        return 'vrooooom!'

    # TODO

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels):
        self.num_wheels = 2

    def drive(self):
        return 'BRAAP!!'


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

vehicles = [
    GroundVehicle(4),
    GroundVehicle(4),
    Motorcycle(2),
    GroundVehicle(4),
    Motorcycle(2),
]

# Go through the vehicles list and print the result of calling drive() on each.

bike = Motorcycle(2)
print('Motorcycle num of wheels: ',bike.num_wheels)
print('Motorcycle sound: ',bike.drive())

car = GroundVehicle(4)
print('car num of wheels: ',car.num_wheels)
print('car sound: ',car.drive())


# TODO
