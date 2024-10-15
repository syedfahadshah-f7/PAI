from abc import ABC, abstractmethod
from datetime import date

class Vehicle(ABC):
    def __init__(self, make, model, rent, status):
        self.make = make
        self.model = model
        self.rent = rent
        self.status = status
    
    @abstractmethod
    def availability(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def cal_rent(self, hours):
        pass

    def returned(self):
        if not self.status:
            self.status = True

    def booked(self):
        if self.status:
            self.status = False

class Car(Vehicle):
    def availability(self):
        return self.status
    
    def display(self):
        print(f"Car - Make: {self.make}, Model: {self.model}, Rent: {self.rent}, Availability: {self.status}")
        
    def cal_rent(self, hours):
        print(f"Total Rent for {hours} hours: {self.rent * hours}")

class SUV(Vehicle):
    def availability(self):
        return self.status
    
    def display(self):
        print(f"SUV - Make: {self.make}, Model: {self.model}, Rent: {self.rent}, Availability: {self.status}")
        
    def cal_rent(self, hours):
        print(f"Total Rent for {hours} hours: {self.rent * hours}")

class Truck(Vehicle):
    def availability(self):
        return self.status
    
    def display(self):
        print(f"Truck - Make: {self.make}, Model: {self.model}, Rent: {self.rent}, Availability: {self.status}")
        
    def cal_rent(self, hours):
        print(f"Total Rent for {hours} hours: {self.rent * hours}")


class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []

    def rent_vehicle(self, vehicle, rental_reservation):
        vehicle.booked()
        self.rental_history.append(rental_reservation)

    def display_rental_history(self):
        print(f"Rental History for {self.name}:")
        for rental in self.rental_history:
            rental.display()


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
    
    def display(self):
        print(f"Reservation for {self.customer.name}:")
        print(f"Vehicle: {self.vehicle.make} {self.vehicle.model}")
        print(f"Start Date: {self.start_date}, End Date: {self.end_date}")
        print(f"Rental Duration: {(self.end_date - self.start_date).days} days")
        self.vehicle.display()


def display_details(obj):
    obj.display()


car = Car("Toyota", 2020, 50, True)
suv = SUV("Ford", 2021, 80, True)
truck = Truck("Mercedes", 2019, 120, True)

customer1 = Customer("Syed Fahad Shah", "k230062@nu.edu.pk")
rental1 = RentalReservation(customer1, car, date(2023, 9, 20), date(2023, 9, 25))


customer1.rent_vehicle(car, rental1)


display_details(car)
display_details(rental1)


customer1.display_rental_history()
