# Write a Car class that has the following properties: registration number, maximum speed, current speed.....
import random


class Car:
    def __init__(self, reg_num, max_speed, current_speed=0, travel_distance=0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance


car = Car("ABC-123", 142)
print("")  
print(f"New car registration number :{car.reg_num}\nmax_speed :{car.max_speed} km/h\ncurrent_speed :{car.current_speed} km/h\ncurrent_speed :{car.travel_distance} km")

print("-------------------------------------------------------------------")  
print("")

# 2 Extend the program by adding an accelerate method into the new class. The method should receive ..


class Car:
    def __init__(self, reg_num, max_speed, current_speed=0, travel_distance=0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

    def accelerate(self, speed):
        new_speed = self.current_speed + speed
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed

        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed


car = Car("ABC-123", 142)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"current speed: {car.current_speed} km/h")

car.accelerate(-200)
print(f"Final speed: {car.current_speed} km/h")
print("-------------------------------------------------------------------")
print("")

# 3   Again, extend the program by adding a new drive method that receives the number of hours as a
class Car:
    def __init__(self, reg_num, max_speed, current_speed=0, travel_distance=0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

    def accelerate(self, speed):
        new_speed = self.current_speed + speed
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed

        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travel_distance = 2000
        self.travel_distance += self.current_speed * hours


car = Car("ABC-123", 142)
car.accelerate(60)
print(f"current speed: {car.current_speed} km/h")

car.drive(1.5)
print(f"Travel distance after driving 1.5hr : {int(car.travel_distance)} km")

print("-------------------------------------------------------------------")
print("")

# 4. Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginnin


class Car:
    def __init__(self, reg_num, max_speed, current_speed=0, travel_distance=0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

    def accelerate(self, speed):
        new_speed = self.current_speed + speed
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed

        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travel_distance += self.current_speed * hours


cars = []
for car in range(10):
    max_speed = random.randint(100, 200)
    reg_num = f"ABC-{car + 1}"
    cars.append(Car(reg_num, max_speed))

hours = 0
race_ongoing = True
while race_ongoing:
    hours += 1
    for car in cars:
        change_speed = random.randint(-10, 15)
        car.accelerate(change_speed)

        car.drive(1)

        if car.travel_distance >= 10000:
            race_ongoing = False
            break

print(f"Race completed in {hours} hours.")
print("Registration Number | Current Speed | Max Speed | Traveled distance")
print("-------------------------------------------------------------------")
for car in cars:
    print(f"{car.reg_num:<19} | {car.current_speed:<13} | {car.max_speed:<9} | {car.travel_distance:<17}")
