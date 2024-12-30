class Spiderman:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 def describeSpiderman(self):
  print(f"Name: {self.name} Age: {self.age}")
class Tobey(Spiderman):
 def __init__(self, name, age, movieTitle):
  super().__init__(name, age)
  self.movieTitle = movieTitle
class Andrew(Spiderman):
 def __init__(self, name, age, movieTitle):
  super().__init__(name, age)
  self.movieTitle = movieTitle
class Tom(Spiderman):
 def __init__(self, name, age, movieTitle):
  super().__init__(name, age)
  self.movieTitle = movieTitle
tobey = Tobey("tobey", 30, "Spider-man")
andrew = Andrew("andrew", 35, "The Amazing Spider-man")
tom = Tom("tom", 25, "Spider-man: Homecoming")
print(f"{tobey.name.upper()} starred in {tobey.movieTitle}")
print(f"{andrew.name.upper()} starred in {andrew.movieTitle}")
print(f"{tom.name.upper()} starred in {tom.movieTitle}")