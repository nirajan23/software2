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

