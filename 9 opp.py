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
        # Accumulate the distance traveled
        self.travel_distance += self.current_speed * hours


# Initialize the race with 10 cars
cars = []
for i in range(10):
    max_speed = random.randint(100, 200)
    reg_num = f"ABC-{i+1}"
    cars.append(Car(reg_num, max_speed))

# Start the race
race_ongoing = True
hours = 0
while race_ongoing:
    hours += 1
    for car in cars:
        # Random speed change between -10 km/h and +15 km/h
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)

        # Each car drives for 1 hour at the current speed
        car.drive(1)

        # Check if any car has reached or exceeded 10,000 km
        if car.travel_distance >= 10000:
            race_ongoing = False
            break

# Display race results
print(f"\nRace completed in {hours} hours.\n")
print("Registration | Max Speed | Current Speed | Travel Distance")
print("----------------------------------------------------------")
for car in cars:
    print(f"{car.reg_num:<12} | {car.max_speed:<9} | {car.current_speed:<13} | {int(car.travel_distance):<15}")
