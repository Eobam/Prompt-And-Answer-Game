import inspect
import time
import threading
import random
import time2 as t


#Player attributes

p_health = 100

p_speed = 20


damage_am = int((0))

BLANK = False

class Item:
    def __init__(self, rarity, healing, heal_amount, damage, pull_count ):
        self.rarity = rarity
        self.healing = healing
        self.heal_amount = heal_amount
        self.damage = damage
        self.pull_count = pull_count




    def heal(self):
        p_health
        if self.healing:
            p_health
            p_health = self.heal_amount + p_health
            if p_health > 100:
                p_health = p_health - (p_health - 100) 


class Weapon:
    def __init__(self, damage, attack_speed):
        self.damage = damage
        self.attack_speed = attack_speed



class Enemy:
    def __init__(self, health, damage, attack_speed, last_attack):
        self.last_attack = time.time()
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed
    def take_damage(self, damage_amount):
        self.health -= damage_amount
        print(f"Enemy health is now {self.health}")

tutorial_zombie = Enemy(30, 5, 5, time.time())
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




def enemy_attack(enemy, damage_amount, attack_speed, health):
    global p_health

    if health <= 0 or p_health <= 0:
        print("DEBUG: health of player or zombie is 0")
        return p_health
    
    while p_health > 0 and health > 0:
        if (time.time() - enemy.last_attack) >= attack_speed:
            p_health -= damage_amount
            enemy.last_attack = time.time()

    print("You got attacked!")
    print(f"Your health is now {p_health}")
    return p_health



print("Ok, so you can look at what you have, let's see if you can take away what someone else has (their health)")
time.sleep(0.6)
print("Let's redo this scene")
time.sleep(0.6)
print(f"You're still in Dessert-Town, but now, there's a zombie, runnning at you, in your hands, you have nothing, just your fists, and neither does the zombie. ~You now have fists in your inventory and they are equipped the zombie has {tutorial_zombie.health} health~") #Use .sleep to create a timed scene, add fists to inventory.
time.sleep(1.0)
print(f"You have {tutorial_zombie.attack_speed} seconds before it attacks you, try and attack it with attack_e! btw you have {p_health} health and the fists do {fists.damage} damage")

current_command = input("Alright, make your move!")
enemy_attack(tutorial_zombie, tutorial_zombie.damage, tutorial_zombie.attack_speed, tutorial_zombie.health)
print(tutorial_zombie.health)
print(f"DEBUG:{current_command}")


pulled_item = "blank"

def item_list(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,):
    item_list = [item1, item2, item3, item4, item6, item7, item8, item9, item10]
    reitem1 = item1
    reitem2 = item2
    reitem3 = item3
    reitem4 = item4
    reitem5 = item5
    reitem6 = item6
    reitem7 = item7
    reitem8 = item8
    reitem9 = item9
    reitem10 = item10

    pulled_item = random.choice(item1, item2, item3, item4, item6, item7, item8, item9, item10)
    while pulled_item == "blank":
        pulled_item = random.choice(item1, item2, item3, item4, item6, item7, item8, item9, item10)
        if pulled_item != "blank":
            item_list(reitem1, reitem2, reitem3, reitem4, reitem5, reitem6, reitem7, reitem8, reitem9, reitem10)
    if pulled_item.rarity == ("Uncommon"):
        pulled_item.pull_count += 1
        pulled_item = random.item_list
        if Item.rarity("Uncommon") and Item.pull_count == 2:
            return pulled_item
        

if current_command == "e" or current_command == "attack_e":
    pass
else:
    current_command = input("Invalid input, please restate what you would like to do.") 

if commands_on == True:
    if current_command == "attack_e":
        attack_enemy = True
        tutorial_zombie.take_damage(fists.damage)
        print(f"Enemy attacked their health is now {tutorial_zombie.health}")
    if current_command == "e":
        open_inventory()

print(f"DEBUG:{current_command}")
print(tutorial_zombie.health)

if tutorial_zombie.health <= 0:
    e_p_alive = False

print("Nice job! Now quick, attack again before it hits you!")
while tutorial_zombie.health > 0 and p_health > 0: 
    current_command = input("Make your move:")
    if current_command == "e" or current_command == "attack_e":
        pass
    else:
        current_command = input("Invalid input, please restate what you would like to do.") 

    if commands_on == True:
        if current_command == "attack_e":
            attack_enemy = True
            tutorial_zombie.take_damage(fists.damage)
            print("Enemy attacked")
        if current_command == "e":
            open_inventory()


if tutorial_zombie.health <= 0:
    print("Nice job! Now that you've got the fighting aspect down, let's explore a bit!")



print("Ok, so you're looking at this dead zombie, you see something in what seemed to be it's jean pocket, if you want to pick it up, put your input as: search ")

current_command = input("What do you want to do?")

if current_command == "e" or current_command == "attack_e":
        pass
else:
        current_command = input("Invalid input, please restate what you would like to do.") 


Basic_Bandage = Item("Common", True, 10, 0, 0)

Stick = Item("Common", False, 0, 3, 0)

Grandmas_Sword = Item("Uncommon", False, 0, 6, 0)



item_list(Basic_Bandage, Stick, Grandmas_Sword, "blank", "blank", "blank", "blank", "blank", "blank", "blank")

if commands_on == True:
    if current_command == "attack_e":
            attack_enemy = True
            tutorial_zombie.take_damage(fists.damage)
            print("Enemy attacked")
    if current_command == "e":
            
      open_inventory()
    if current_command == "search":
        print(f"You got a {pulled_item}")

print("Nice! Now check your inventory to look at your new item!")

