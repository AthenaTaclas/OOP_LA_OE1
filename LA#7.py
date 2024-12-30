class Car:
 def __init__(self, brand, color):
  self.brand = brand
  self.color = color
car1 = Car("Ferrari", "Red")
print("First Car Brand and Color: ", car1.brand, car1.color)
car1.color = "Blue"
print("Updated Color of First Car: ", car1.color)
car2 = Car("Lamborghini", "Green")
print("Second Car Brand and Color: ", car2.brand, car2.color)
car1.color = "Pink"
print("First Car Brand and Color: ", car1.brand, car1.color)
car2.color = "Rainbow"
print("Second Car Brand and Color: ", car2.brand, car2.color)