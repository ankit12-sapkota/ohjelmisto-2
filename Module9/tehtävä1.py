#Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled
#  distance. Add a class initializer that sets the first two of the properties based on parameter values.
#  The current speed and travelled distance of a new car must be automatically set to zero.
#  Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
#  Finally, print out all the properties of the new car.



class Auto:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def default_print(self):
        print(f"registration_number: {self.registration}")
        print(f"Max Speed: {self.max_speed} km/hr")
        print(f"current_speed: {self.current_speed} km/hr")
        print(f"travelled_distance: {self.travelled_distance} km")


new_car = Auto("ABC_123", 140)
new_car.default_print()



