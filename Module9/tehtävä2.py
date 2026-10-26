#Extend the program by adding an accelerate method into the new class. The method should receive the change of speed (km/h) as a parameter. If the change is negative, the car reduces speed. 
# The method must change the value of the speed property of the object.
#  The speed of the car must stay below the set maximum and cannot be less than zero. 
# Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. 
# Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
#  The travelled distance does not have to be updated yet.

class auto:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def acceleration(self, speed):
        self.current_speed = self.current_speed + speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

new_car = auto("CPM-151", 400)

# accelerating by 30 km/hr
new_car.acceleration(30)

# accelerating by 70 km/hr
new_car.acceleration(70)

# accelerating by 50 km/hr
new_car.acceleration(50)

print(f"The current speed is : {new_car.current_speed}")
#emergency braking 
new_car.acceleration(-200)
print(f"The current speed is : {new_car.current_speed}")

                
                
        
        