import random
    
class auto:

    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def acceleration(self, speed):
        self.current_speed += speed
        if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
        elif self.current_speed < 0:
                self.current_speed = 0

    def drive(self, hour):
        self.travelled_distance += self.current_speed * hour
        

car_object = []  
for i in range(1, 11):
    registration = f"ABC-{i}"
    max_speed = random.randint(100, 200)

    car = auto(registration, max_speed)
    car_object.append(car)



class Race:

    def __init__(self, name, distance_km, car_object):
         self.name = name
         self.distance_km = distance_km
         self.car_object = car_object

    def hour_passes(self):
        for car in self.car_object:
            speed = random.randint(-10, 15)
            car.acceleration(speed)
            
            car.drive(1)
    def print_status(self):
        print((f"{'Registration':<15} {'Max Speed':<12} {'Current Speed':<15} {'Distance':<15}"))
        print("-" * 60)

        for cars in self.car_object:
            print(f"{cars.registration:<15} {cars.max_speed:<15} {cars.current_speed:<15} {cars.travelled_distance:<15}" )
              

    def race_finished(self):       
        race_finished = False
        for car in self.car_object:
            if car.travelled_distance >= self.distance_km:
                race_finished = True
                break
            
        return race_finished
            

race1 = Race("Grand Demolition Derby", 8000, car_object)

hours = 0

while not race1.race_finished():
    race1.hour_passes()
    hours + 1

    if hours % 10 == 0:
        race1.print_status()

race1.print_status()        
         
              
              
              
         