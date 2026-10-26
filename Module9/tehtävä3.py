#Again extend the program by adding a new drive method that receives the number of hours as a parameter. 
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.


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

    def car_drive(self, hour):
        self.travelled_distance = self.travelled_distance + (self.current_speed * hour)


new_car = auto("CPM-151", 220 )  
new_car.acceleration(60)
new_car.car_drive(2)
new_car.car_drive(3)
print(f"The car new travelled distance is {new_car.travelled_distance}" )              
