class Car:

    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def car_drive(self, hour):
        self.travelled_distance += hour * self.current_speed




class ElectricCar(Car):
    def __init__(self, registration, max_speed, capacity):
        super().__init__(registration, max_speed)
        self.capacity = capacity

class GasolineCar(Car):
    def __init__(self, registration, max_speed, gasoline):
        super().__init__(registration, max_speed) 
        self.gasoline = gasoline 

electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165 , 32.3)

electric.current_speed = 170
gasoline.current_speed = 150
electric.car_drive(3)
gasoline.car_drive(3)

print(f"The electric car has travelled {electric.travelled_distance} km")
print(f"The gasoline car has travelled {gasoline.travelled_distance} km")