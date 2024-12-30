class Appliance:
 def __init__(self, brand, model):
  self.brand = brand
  self.model = model
 def operate(self):
  print("Operating!")
 def info(self):
  print(f"Brand: {self.brand}\nModel: {self.model}")
class WashingMachine(Appliance):
 def operate(self):
  print("Washing Clothes!")
class Refrigerator(Appliance):
 def operate(self):
  print("Keeping food cold!")
class Microwave(Appliance):
 def operate(self):
  print("Heating food!")
washing_machine = WashingMachine("Astron", "Hanabishi")
refrigerator = Refrigerator("Toshiba", "Condura")
microwave = Microwave("Asahi", "Samsung")
appliances = [washing_machine, refrigerator, microwave]
for appliance in appliances:
  appliance.info()
  appliance.operate()
  print()
