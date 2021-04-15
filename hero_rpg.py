


# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee





# parent class
class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        

    def alive(self):
        if self.health > 0:
            return True
    def print_status(self):
        print(f"Youu have {self.health} health and {self.power} power.")

    def print_status(self):
        if self == goblin:
            print_status(self)
            print(f"The goblin has {self.health} health and {self.power} power.")
        elif self == Hero:
            print_status(self)
            print(f"The hero has {self.health} health and {self.power} power.")



#child class
class Hero(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
    
    
    
    
    
    # def __init__(self, health, power):
    #     super().__init__(health, power)
    #     self = "Hero"
    # def charType(self)
    #     self.health = health
    #     self.power = power
    

        

        # if goblin.health > 0:


    
#child class    
class Goblin(Character):
    def charType(self)
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
    charType.self(Character)
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)



    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while goblin.alive() and hero.alive():
        # print("You have {} health and {} power.".format(hero.health, hero.power))
        # print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
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
                goblin.print_status()
            else:
                print('Goblin is dead')
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            # Goblin.attack(enemy)
            hero.health -= goblin.power
            # print("The goblin does {} damage to you.".format(goblin.power))
            if hero.alive():
                hero.print_status()
            else:
                print(f"You are dead.")
            # goblin.health -= hero.power
            # print("You do {} damage to the goblin.".format(hero.power))
            # if goblin.health <= 0:
            #     print("The goblin is dead.")


main()




    



#             goblin_health -= hero_power
#             print("You do {} damage to the goblin.".format(hero_power))
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:














