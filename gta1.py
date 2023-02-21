 #Python Text-Based Game: Grand Theft Auto 1
import random
 
#Setting up the game 
name = input("What is your name? ")
print("Welcome to Grand Theft Auto 1, " + name + "!")
 
#Game engine
hp = 100
coins = 0
while hp > 0:
    print("Your HP is " + str(hp))
    print("You have " + str(coins) + " coins.")
    print("What would you like to do? You can fight, shop, or quit.")
    action = input("> ")
    if action == "fight":
        enemyHP = random.randint(20, 50)
        print("You have encountered an enemy!")
        print("The enemy has " + str(enemyHP) + " HP")
        while enemyHP > 0 and hp > 0:
            print("What would you like to do? You can attack or flee.")
            fight_action = input("> ")
            if fight_action == "attack":
                dmg = random.randint(10, 20)
                enemyHP = enemyHP - dmg
                print("You have dealt " + str(dmg) + " damage to your enemy.")
                if enemyHP <= 0:
                    print("You have defeated your enemy!")
                    coins = coins + 10
                else:
                    enemy_dmg = random.randint(10, 20)
                    hp = hp - enemy_dmg
                    print("Your enemy has dealt " + str(enemy_dmg) + " damage to you.")
            elif fight_action == "flee":
                print("You have successfully fled from the enemy!")
                break
            else:
                print("Invalid command!")
    elif action == "shop":
        print("Welcome to the shop! You can buy health potions and weapons here.")
        print("What would you like to buy? You can buy a health potion or a weapon.")
        shop_action = input("> ")
        if shop_action == "health potion":
            if coins >= 10:
                hp = hp + 50
                coins = coins - 10
                print("You have successfully bought a health potion and restored your health!")
