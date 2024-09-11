class Vehicle:
    def __init__(self,seating_capacity) -> None:
        self.seating_capacity = seating_capacity
        self.fare = seating_capacity *100


class Bus(Vehicle):
    
    def __init__(self, seating_capacity) -> None:
        super().__init__(seating_capacity)
        self.fare += self.fare *0.1
        

bus1 = Bus(55)        
print(f"Bus fare : {bus1.fare}")
