class Player:
 def __init__(self, name, health, attack_power):
  self.name = name
  self.health = health
  self.attack_power = attack_power
 def attack(self, target):
  target.health -= self.attack_power
  print(f"{self.name} attacked {target.name} for {self.attack_power} damage.")
  print(f"{target.name} has {target.health} health remaining.")
 def heal(self, amount):
  self.health += amount
  print(f"{self.name} healed for {amount} health.")
  print(f"{self.name} now has {self.health} health.")
juan = Player("Juan", 100, 20)
mario = Player("Mario", 80, 15)
while True:
 juan.attack(mario)
 if mario.health <= 0:
  print(f"{juan.name} wins!")
  break
 mario.attack(juan)
 if juan.health <= 0:
  print(f"{mario.name} wins!")
  break
juan.heal(10)
mario.heal(15)
