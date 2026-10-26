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
        

race_car = []    
for i in range(1, 11):
    registration = f"ABC-{i}"
    max_speed = random.randint(100, 200)

    car = auto(registration, max_speed)
    race_car.append(car)


while True:
    for car in race_car:
         speed = random.randint(-10, 15)
         car.acceleration(speed)

         car.drive(1)

    race_finished = False

    for car in race_car:
         if car.travelled_distance >= 1000:
              race_finished = True
              break

    if race_finished:
              break

         

for car in race_car:
    print(car.registration, car.max_speed, car.current_speed, car.travelled_distance)

     





