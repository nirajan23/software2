class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} say Woff!! woff!!")
    def get_breed(self):
        return self.breed
    def set_breed(self,breed):
        self.breed=breed

dog = Dog("Kalu", "street dog")
dog2 =Dog("kali",  "Bull dog")
print(f"name :{dog.name},\nbreed:{dog.breed}")
dog.bark()
print(f"name :{dog2.name},\nbreed:{dog2.breed}")

kennel = [dog, dog2]
for dog in kennel:
    print(f"{dog.name} is kennel")


#def increase_speed_by(self,speed):
    #self.current_speed = speed


    def accelerate(self, speed):
        new_speed = self.current_speed + speed
        if speed > self.max_speed:
            speed = self.max_speed

        elif speed < 0:
            speed = 0

        self.current_speed = speed

import random

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor  # Start at the bottom floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor selection.")
            return

        print(f"Moving to floor {target_floor}...")

        # Move up or down to the target floor
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

        print(f"Elevator has arrived at floor {self.current_floor}")

# Test the Elevator class
elevator = Elevator(bottom_floor=1, top_floor=10)

# Move to a specified floor and then back to the bottom floor
elevator.go_to_floor(5)
elevator.go_to_floor(1)  # Return to the bottom floor


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("INVALID FLOOR SELECTION")
            return

        print(f"Moving to floor {target_floor}...")

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

        print(f"Elevator has arrived at floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number.")


# Test the Building class and run elevators
building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

# Run some elevators to test
building.run_elevator(0, 5)  # Run elevator 0 to the 5th floor
building.run_elevator(1, 8)  # Run elevator 1 to the 8th floor
building.run_elevator(2, 3)  # Run elevator 2 to the 3rd floor
building.run_elevator(0, 1)  # Return elevator 0 to the bottom floor


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor  # Start at the bottom floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor selection.")
            return

        # Move to the target floor and print each floor as it moves
        while self.current_floor < target_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
        while self.current_floor > target_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

        print(f"Elevator has arrived at floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        # Adjust for 1-based index
        if 1 <= elevator_number <= len(self.elevators):
            print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
            self.elevators[elevator_number - 1].go_to_floor(destination_floor)  # Adjust index for 0-based list
        else:
            print("Invalid elevator number.")


# Test the Building and Elevator classes
building = Building(1, 10, 3)

# Run elevators to test functionality with 1-based numbering
building.run_elevator(1, 5)  # Move elevator 1 to the 5th floor
building.run_elevator(2, 8)  # Move elevator 2 to the 8th floor
building.run_elevator(3, 3)  # Move elevator 3 to the 3rd floor
building.run_elevator(1, 1)  # Return elevator 1 to the bottom floor
