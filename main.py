name = input("What's your name?")
input(f"Ok, {name} how are you doing today?")
print("I mean, I don't actually care how your doing an I don't have feelings as I'm a computer program, so let's move on.")
print("Alright, let's set the scene here")
print("Close your eyes (don't actually, just uhhhh, get in the imaginative mindset) and imagine your in the middle of no where, we'll say you're in the town of Dessert-Town, NV, USA, NA, Earth. ")
print("So now that you now where you are, let's get you acquainted to the controls of this.")
print("To open your inventory: press e, to attack an enemy: type attack_e")
current_command = input("Ok, so what do you want to do now?")
print(f"DEBUG: {current_command}")
commands_on = True
def open_inventory():
    print("Inventory opened")
if commands_on == True:
    current_command = "blank"
    if current_command == "attack_e":
        global attack_enemy
        attack_enemy = True
    if current_command == "e":
        open_inventory()
