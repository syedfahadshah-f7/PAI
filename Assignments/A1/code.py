from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, habitat, status) -> None:
        self.name = name
        self.age = age
        self.habitat = habitat
        self.status = status

    @abstractmethod
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nHabitat: {self.habitat} \nStatus: {self.status}")

    def Mark_Availability(self, status):
        self.status = status

class Mammals(Animal):
    def __init__(self, name, age, habitat, fur_length, diet_type, status) -> None:
        super().__init__(name, age, habitat,status)
        self.fur_length = fur_length
        self.diet_type = diet_type
        

    def display(self):
        super().display()
        print(f"Fur Length: {self.fur_length}\nDiet Type: {self.diet_type}\n")

class Birds(Animal):
    def __init__(self, name, age, habitat, wingspan, flight_altitude,status) -> None:
        super().__init__(name, age, habitat,status)
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude
 
    def display(self):
        super().display()
        print(f"Wingspan: {self.wingspan}\nFlight Altitude: {self.flight_altitude}\n")

class Reptiles(Animal):  
    def __init__(self, name, age, habitat, scale_pattern, venomous: bool,status) -> None:
        super().__init__(name, age, habitat,status)
        self.scale_pattern = scale_pattern
        self.venomous = venomous

    def display(self):
        super().display()
        print(f"Scale Pattern: {self.scale_pattern}\nVenomous: {self.venomous}\n")


if __name__ == "__main__":
    # Create Mammals object
    mammal = Mammals("Tiger", 5, "Forest", "Short", "Carnivore", "Quarantine")
    mammal.display()

    # Create Birds object
    bird = Birds("Eagle", 3, "Mountains", 2.5, 5000,"Available")
    bird.display()

    # Create Reptiles object
    reptile = Reptiles("Cobra", 2, "Jungle", "Smooth", True,"Quarantine") 
    reptile.display()
    
    print(f"Changing Availability Of Each Anmials:\n")
    mammal.Mark_Availability("Available")
    reptile.Mark_Availability("Available")
    bird.Mark_Availability("Quarantine")
    mammal.display()
    bird.display()
    reptile.display()
    
