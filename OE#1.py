class GameCharacter:
    def __init__(self, name, level, health_points):
        self.name = name
        self.level = level
        self.health_points = health_points
       
    def attack(self):
        print(f"{self.name} attacks and deals {self.level * 10} damage.")
           
    def __str__(self):
        return (f"Character Name: {self.name}, Level: {self.level}, HP: {self.health_points}.")
   
class WeaponUpgrade(GameCharacter):
    def __init__(self, name, level, health_points, weapon_name, weapon_damage):
        super().__init__(name, level, health_points)
        self.weapon_name = weapon_name
        self.weapon_damage = weapon_damage
       
    def use_weapon(self):
        print(f"{self.name} uses the {self.weapon_name} and deals {self.weapon_damage + (self.level * 10)} damage.")
       
Link = GameCharacter("Link", 100, 150)
Samus = WeaponUpgrade("Samus", 10, 500, "Plasma Beam", 350)

Link.attack()
Samus.attack()
Samus.use_weapon()
print(Samus)