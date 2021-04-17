


# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee





# parent class
class Character():
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def attack(self, enemy):
        enemy.health -= self.power
        # print("You did {} damage to the goblin".format(self.power))
    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        print(f"{self.name} have {self.health} health and {self.power} power.")

    # def print_status(self):
    #     if self == goblin:
    #         print_status(self)
    #         print(f"The goblin has {self.health} health and {self.power} power.")
    #     elif self == Hero:
    #         print_status(self)
    #         print(f"The hero has {self.health} health and {self.power} power.")



#child class
class Hero(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
    # def __init attack(self, enemy):
    #     enemy.health -= self.power
    #     print("You do {} damage to the goblin.".format(self.power))
    # def __init__ (self, health, power, name):
    #     self.health = health
    #     self.power = power
    #     self.name = name


class Goblin(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name


class Zombie(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
    
    
    
    
    
    # def __init__(self, health, power):
    #     super().__init__(health, power)
    #     self = "Hero"
    # def charType(self)
    #     self.health = health
    #     self.power = power
    

        

        # if goblin.health > 0:


    
#child class    
    # def __init__(self, health, power):
    #     super().__init__(health, power)

    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print("The goblin does {} damage to you.".format(self.power))
        
        
    # def print_status(self):
    #     print(f"The goblin has {self.health} health and {self.power} power.")
        
        
        # if hero.health <= 0:
        #     print("You are dead.")
    # def charType(self, enemy)

        # self.health = health
        # self.power = power


        




def main():
    # charType.self(Character)
    hero = Hero(10, 5, "Hero")
    goblin = Goblin(6, 2, "Goblin")
    zombie = Zombie(1000, 4, "Zombie")



    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while goblin.alive() and hero.alive():
        # hero.health -= goblin.power
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        # goblin.health -= hero.power
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
            if goblin.alive():
                print("You did {} damage to the Goblin.".format(hero.power))
                hero.health -= goblin.power
                print("Goblin did {} damage to you.".format(goblin.power))
                # goblin.print_status()
            else:
                print("You did {} damage to the goblin.".format(hero.power))
                print('The Goblin is dead.')
        elif raw_input == "2":
            print("Goblin did {} damage to you.".format(goblin.power))
            hero.health -= goblin.power
        elif raw_input >= "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

            if goblin.health > 0:
                print("He's still alive.".format(goblin.power))
            else:
                goblin.attack(hero)
            # hero.health -= goblin.power
            # print("The goblin does {} damage to you.".format(goblin.power))
            if hero.alive():
                # hero.print_status()
                # print("You did {} damage to the goblin.".format(hero.power))
                print("You survived. You Win!!! ".format(goblin.power))
                # hero.print_status()
            else:

                print("You are dead.")
            # goblin.health -= hero.power
            # if goblin.health <= 0:
            #     print("The goblin is dead.")


main()




    



# #             goblin_health -= hero_power
# #             print("You do {} damage to the goblin.".format(hero_power))
# #             if goblin_health <= 0:
# #                 print("The goblin is dead.")
# #         elif raw_input == "2":
# #             pass
# #         elif raw_input == "3":
# #             print("Goodbye.")
# #             break
# #         else:
# #             print("Invalid input {}".format(raw_input))

# #         if goblin_health > 0:






# #double hit
# def attack(self, opponent):
#         if random.randint(0,100) < 20:
#             opponent.Health -= (self.Power * 2)
#             print("{} does double damage({}) to {}.".format(self.name, (self.Power * 2), opponent.name))
#         else:
#             opponent.Health -= self.Power
#             print("{} does {} damage to {}.".format(self.name, self.Power, opponent.name))








# #medic and shadow

# def attack(self, enemy):
#         if enemy.name == "zombie": 
#             print("Zombie can not die!")

#         if enemy.name == "shadow" and random.randint(0,10) < 1:
#             enemy.health -= (self.power)
#             # print("{} does damage {} to {}.".format(self.name, self.power , enemy.name))
        
#         elif enemy.name == "shadow":
#             print("no damage")    
        
#         elif enemy.name == "medic" and random.randint(0,100) < 20:
#             enemy.health -= (self.power * 2)
#             print("{} does double damage({}) to {}.".format(self.name, (self.power * 2), enemy.name))
        
#         else:
#             enemy.health -= self.power
#             print("{} does {} damage to {}.".format(self.name, self.power, enemy.name))






