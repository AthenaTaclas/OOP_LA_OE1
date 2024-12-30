class Dog:
 def __init__(self, name):
  self.name = name
 def speak(self):
  print("Dog: Bark!")
class Cat:
 def __init__(self, name):
  self.name = name
 def speak(self):
  print("Cat: Meow!")
class Bird:
 def __init__(self, name):
  self.name = name
 def speak(self):
  print("Bird: Chirp!")
class Fish:
 def __init__(self, name):
  self.name = name
 def speak(self):
  print("Fish: ...")
dog = Dog("Bantay")
cat = Cat("Luna")
bird = Bird("Tweety")
fish = Fish("Nemo")
def animal_sounds(animal):
 animal.speak()
animals = [dog, cat, bird, fish]
for animal in animals:
 animal_sounds(animal)