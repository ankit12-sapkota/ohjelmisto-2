class Elevator:

    def __init__(self,bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Your are on floor {self.current_floor}.")
        else:
            print(f"You are on floor {self.top}.")
        

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Your are on floor {self.current_floor}.")
        else:
            print(f"You are on floor {self.bottom}.")

    def go_to_floor(self, destination):
        if destination < self.bottom or destination > self.top:
            print("invalid floor")
            return
        while True:
            if self.current_floor == destination:
                print(f"Please exit the elevator.")
                break
            elif self.current_floor < destination:
               self.floor_up()
            else:
                self.floor_down()
class Building:
       

    def __init__(self,bottom,top, elevator_count):
        self.top = top
        self.bottom = bottom
        self.elevator_count = elevator_count
        self.elevator_list = []
        self.create_elevator()

    def create_elevator(self):
        for i in range(self.elevator_count):
            new_elevator = Elevator(self.bottom, self.top)
            self.elevator_list.append(new_elevator)

    def run_elevator(self, lift_number, destination):
        lift_count = len(self.elevator_list)
        if lift_number < 1 or lift_number > lift_count:
            print(f"There are only {len(self.elevator_list)} elevator in the building.")
        else:
            lift_in_use = self.elevator_list[lift_number - 1]
            lift_in_use.go_to_floor(destination)

    def fire_alarm(self):
        for l in self.elevator_list:
            l.go_to_floor(l.bottom)
        print("All elevator to the bottom floor.") 

building1 = Building(1, 12, 5)
building1.fire_alarm()

            

            