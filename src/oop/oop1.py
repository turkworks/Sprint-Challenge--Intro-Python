# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    # Base Class
    def __init__(self):
        print('Engine is running')


Vehicle()


class FlightVehicle(Vehicle):
    # Child Class
    def __init__(self):
        Vehicle()
        print('Wings have been inspected')


FlightVehicle()


class Airplane(FlightVehicle):
    # Grandchild Class
    def __init__(self):
        FlightVehicle()
        print("Airplane is cruising at 5,000 feet")


Airplane()


class Starship(FlightVehicle):
    # Grandchild Class
    def __init__(self):
        FlightVehicle()
        print('lightspeed engaged')


Starship()


class GroundVehicle(Vehicle):
    # Child Class
    def __init__(self):
        Vehicle()
        print('lights are on')


GroundVehicle()


class Car(GroundVehicle):
    # Grandchild Class
    def __init__(self):
        GroundVehicle()
        print('Seat belts are on')


Car()


class Motorcycle(GroundVehicle):
    # Grandchild Class
    def __init__(self):
        GroundVehicle()
        print('helmets are on')


Motorcycle()
