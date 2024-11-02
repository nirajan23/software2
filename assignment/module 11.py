
#1 Implement the following class hiera.......

class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")


book_info = Book("Compartment No. 6", "Rosa Liksom", 192)
book_info.print_information()

print()

magazine_info = Magazine("Donald Duck", "Aki Hyyppä")
magazine_info.print_information()
print("-----------------------------------------------------")

#2.Extend the previosly written Car class by adding two subclasses: ElectricCar...

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

class ElectricCar(Car):
    def __init__(self,reg_num, max_speed, battery_capacity):
        super().__init__(reg_num,max_speed)
        self.battery_capacity = battery_capacity

    def print_travel_distance(self):
        print(f"\nTravel distance of Electric car {self.reg_num} is {self.travel_distance:.2f} km")


class GasolineCar(Car):
    def __init__(self,reg_num, max_speed, tank_volume):
        super().__init__(reg_num,max_speed)
        self.tank_volume = tank_volume

    def print_travel_distance(self):
        print(f"Travel distance of Gasoline car {self.reg_num} is {self.travel_distance:.2f} km")


electricCar =ElectricCar("ABC-15",180, 52.5)
gasolineCar =GasolineCar("ACD-123", 165,32.3)

electricCar.accelerate(80)
electricCar.drive(3)
gasolineCar.accelerate(100)
gasolineCar.drive(3)

electricCar.print_travel_distance()
gasolineCar.print_travel_distance()