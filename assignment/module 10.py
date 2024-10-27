

#1 Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.........
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"you are at {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"you are at {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("INVALID FLOOR SELECTION")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

        print(f"Elevator has arrived at floor {self.current_floor}\n")


elevator = Elevator(1, 10)

elevator.go_to_floor(4)
elevator.go_to_floor(9)
elevator.go_to_floor(1)
print("----------------------------------------")



#2...........
class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 1 <= elevator_number <= len(self.elevators):
            print(f"Running elevator {elevator_number} to floor {destination_floor}")
            self.elevators[elevator_number - 1].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number.")

building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

building.run_elevator(1, 9) 
building.run_elevator(2, 3) 
building.run_elevator(3, 5) 

