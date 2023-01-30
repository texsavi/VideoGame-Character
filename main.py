import random
s=" "
print(f"{s:^20}\033[32m*Game Z00NE*")
print()


class char:
  name = None
  health = None
  mP = None
  lives=None
  type=None
  strength=None
  speed=None


  def __init__(self, name, health, mP, lives, type, strength, speed):
    self.name = name
    self.health = health
    self.mP = mP
    self.lives = lives

  def play(self):
    print(
      f"""Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.mP}\nLives: {self.lives}""")
    print()

  def vamp(self):
    print(
      f"""Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.mP}\nType: {self.type}\nStrength: {self.strength}\n"""
    )
    dani = ["day", "night"]
    dani = random.choice(dani).capitalize()
    print(f"Day/Night?: {dani}")
    print()

  def orC(self):
    print(
      f"""Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.mP}\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.speed}"""
    )
    print()

class player(char):

  def __init__(self):
    self.name = name
    self.health = health
    self.mP = mP
    self.lives = lives
    
player=char("Stark","157","78","2","","","")
player.play()

class enemy(char):

  def __init__(self,name, health, mP, type, strength, speed):
    self.name = name
    self.health = health
    self.mP = mP
    self.type = type
    self.strength = strength
    self.speed = speed


class orc(enemy):

  def __init__(self):
    self.name = name
    self.health = health
    self.mP = mP
    self.type = type
    self.strength = strength
    self.speed = speed

orc=enemy("Thanos","189","98","Orc","337","999")
orc.orC()

orc=enemy("CM","140","34","Orc","147","52")
orc.orC()

orc=enemy("Krumo","152","45","Orc","140","67")
orc.orC()

   
  
class vampire(enemy):


  def __init__(self):
    self.name = name
    self.health = health
    self.mP = mP
    self.type = type
    self.strength = strength
    self.hour = hours()

vampire=enemy("Frewofl","173","88","Vampire","211","")
vampire.vamp()


vampire=enemy("Niklaus","170","87","Vampire","203","")
vampire.vamp()
