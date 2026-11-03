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

        
                    
        

h = Elevator(1, 10)



h.go_to_floor(10)
h.go_to_floor(1)







    

