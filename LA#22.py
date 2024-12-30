class BirthdayParty:
 def __init__(self, theme, special_d, secret_d):
  self.theme = theme
  self.special_d = special_d
  self.secret_d = secret_d
 def Allfoods(self):
  print(f"""List of Foods
Theme: {self.theme}
Special Dish: {self.special_d}""")
  self._secret()
  print("*"*5)
 def _secret(self):
  print(f"Secret Dish: {self.secret_d}")
theme1 = BirthdayParty("Year End Party", "Spaghetti", "Fried Chicken")
theme1.Allfoods()
theme2 = BirthdayParty("Thaksgiving Party", "Cookies", "Juice")
theme2.Allfoods()
theme3 = BirthdayParty("New Year", "Fruits", "Wine")
theme3.Allfoods()
