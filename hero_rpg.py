


# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee





# parent class
class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def attack(self, enemy):
        enemy.health -= self.power
        
    def alive(self):
        if self.health > 0:
            return True
        
    

    def print_status(self):
        print(f"{self.name} have {self.health} health and {self.power} power.")

    


#child class
class Hero(Character):
    def __init__attack(self, enemy):
        enemy.health -= self.power
    def alive(self, health):
        if self.health > 0:
            return True
        
            

    


class Goblin(Character):
    def __init__attack(self, enemy):
        enemy.health -= self.power

        

class Zombie(Character):
    def __init__attack(self, enemy):
        enemy.health -= self.power
    
    
    


def main():
    # charType.self(Character)
    hero = Hero(10, 5, "Hero")
    goblin = Goblin(6, 2, "Goblin")
    zombie = Zombie(1000, 4, "Zombie")



    

    while goblin.alive() and hero.alive: #and zombie.alive:
        # hero.health -= goblin.power
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        #print("The zombie has {} health and {} power.".format(zombie.health, zombie.power))
        # goblin.health -= hero.power
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        #print("2. fight zombie")
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
                print("You did {} damage to the Goblin.".format(hero.power))
                print('The Goblin is dead.')
            while goblin.health <= 0 and hero.health > 0:
                print("Zombie wants to fight. Do you accept challenge? ")
                print("1. fight zombie")
                print("2. flee from zombie")
                raw_input = input()
                if raw_input == "1":
                    hero.attack(zombie)
                    print(f"You did {hero.power} damage to the Zombie.")
                    hero.health -= zombie.power
                    print(f"Zombie did {zombie.power} damage to you.")
                    while zombie.health < 1000:
                        print("You have {} health and {} power.".format(hero.health, hero.power))
                        print("The zombie has {} health and {} power.".format(zombie.health, zombie.power))
                        print("Do you wish to continue?")
                        raw_input = input()
                        if raw_input == "1":
                            hero.attack(zombie)
                            print(f"You did {hero.power} damage to the Zombie.")
                            hero.health -= zombie.power
                            print(f"Zombie did {zombie.power} damage to you.")
                            if hero.health <= 0:
                                print("You are dead. GAME OVER!!!")
                                break
                        elif raw_input == "2": 
                            print("Bye!!!")
                            break
                        else:
                            if zombie.attack(hero):
                                hero.health <= 0
                                print("You are dead.\nGAME OVER!!!!")
                                break                                 
                else:
                    if raw_input == "2":
                        print("Bye!!! \nGAME OVER!!!!")
                        break
                    else:
                        print("Invalid input {}".format(raw_input))

        
            else:
                pass
            
        elif raw_input == "2":
            goblin.attack(hero)
            print("Goblin did {} damage to you.".format(goblin.power))
            if hero.alive(hero.health):
                print("Dont just stand there, fight!!!")
                
            else:
                print("You are dead. GAME OVER!!!")
                break
            
        elif raw_input >= "3":
            print("Goodbye. Thanks for playing")
            break
        else:
            print("Invalid input {}".format(raw_input))

            if goblin.health > 0:
                print("He's still alive.".format(goblin.power))
            else:
                goblin.attack(hero)
            
            if hero.alive():
                hero.health 
                pass
               
            else:
                print("You are dead.")
            


main()

