class Vehicle:
 def __init__(self, brand, model, fuel_type):
  self.brand = brand
  self.model = model
  self.fuel_type = fuel_type
 def describeVehicle(self):
  print(f"My car Brand {self.brand} the model it is {self.model}, with {self.fuel_type} fuel type")
class Car(Vehicle):
 pass
class Motorcycle(Vehicle):
 pass
toyota = Car("Toyota", "Corolla", "Gasoline")
toyota.describeVehicle()
fazzio = Motorcycle("Fazzio", "Scooter", "Gasoline")
fazzio.describeVehicle()