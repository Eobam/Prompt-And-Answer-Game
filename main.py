import inspect
import time

#Player attributes

p_health = 100

p_speed = 20




damage_am = int((0))

class Weapon:
    def __init__(self, damage, attack_speed):
        self.damage = damage
        self.attack_speed = attack_speed



class Enemy:
    def __init__(self, health, damage, attack_speed):
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed
    def take_damage(self, damage_amount):
        self.health -= damage_amount
        damage_amount = damage_am

tutorial_zombie = Enemy(30, 5, 5)
fists = Weapon(5, 5)
#Beginning intro
name = input("What's your name?")
input(f"Ok, {name} how are you doing today?")
print("I mean, I don't actually care how your doing an I don't have feelings as I'm a computer program, so let's move on.")
time.sleep(0.7)
print("Alright, let's set the scene here")
time.sleep(0.7)
print("Close your eyes (don't actually, just uhhhh, get in the imaginative mindset) and imagine your in the middle of no where, we'll say you're in the town of Dessert-Town, NV, USA, NA, Earth. ")
time.sleep(1.2)
print("So now that you now where you are, let's get you acquainted to the controls of this.")
time.sleep(0.7)
print("To open your inventory: press e, to attack an enemy: type attack_e")
time.sleep(0.7)
print("Try and open your inventory")
inventory_tutorial = True
commands_on = True
current_command = input("Ok, so what do you want to do now?")
while inventory_tutorial == True:
    if current_command != "e":
        print("That's not your inventory!")
        current_command = input("Try again")
    if current_command == "e":
        inventory_tutorial = False 

print(f"DEBUG:{current_command}")
if current_command == "e" or current_command == "attack_e":
    pass
else:
    current_command = input("Invalid input, please restate what you would like to do.")



        

def open_inventory():
    print("Inventory opened")
if commands_on == True:
    if current_command == "attack_e":
        global attack_enemy
        attack_enemy = True
        tutorial_zombie.take_damage(fists.damage)
        print("Enemy attacked")
    if current_command == "e":
        open_inventory()


    if current_command == "e" or current_command == "attack_e":
        pass
    else:
        current_command = input("Invalid input, please restate what you would like to do.") 

print("Ok, so you can look at what you have, let's see if you can take away what someone else has (their health)")
time.sleep(0.6)
print("Let's redo this scene")
time.sleep(0.6)
print(f"You're still in Dessert-Town, but now, there's a zombie, runnning at you, in your hands, you have nothing, just your fists, and neither does the zombie. ~You now have fists in your inventory and they are equipped the zombie has {tutorial_zombie.health} health~") #Use .sleep to create a timed scene, add fists to inventory.
time.sleep(1.0)
print(f"You have {tutorial_zombie.attack_speed} seconds before it attacks you, try and attack it with attack_e! btw you have {p_health} health and the fists do {fists.damage} damage")
current_command = input("Alright, make your move!")
print(Enemy.health)
print(f"DEBUG:{current_command}")

if current_command == "e" or current_command == "attack_e":
    pass
else:
    current_command = input("Invalid input, please restate what you would like to do.") 



