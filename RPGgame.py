# class Chalacter:


#     def __init__(self, health, power):
#         self.health = health,
#         self.power = power,
#         self.name = 'samson'

    
#     def alive(self):
#         if self.health > 0:
#             return True
#         else:
#             return False


#     def attack(self, enemy):
#         enemy.health -= self.power
#         print('{} dose {} damage to the {}'.format(self.name, self.power, enemy.name))
#         if enemy.health <= 0:
#             print('{} is dead'.format(enemy.name))
#         if self.health <= 0:
#             print('{} is dead'.format(self.name))
#     def status(self):
#         print('{} has {} health {} power'.format(self.name, self.health, self.power))


# class HERO(Chalacter):
#     def __init__(self, health, power):
#       super().__init__(health, power)
#       self.name = 'HERO'




# class GOBLIN(Chalacter):
#     def __init__(self, health, power):
#         super().__init__(health, power)
#         self.name = 'GOBLIN'
        



# def main():
#     hero1 = HERO(8, 5)
#     goblin1 = GOBLIN(10, 3)


#     while goblin1.alive and hero1.alive:
#         hero1.status()
#         goblin1.status()
#         print('what do you whant to do?')
#         print('1, fight goblin')
#         print('2, do nothing')
#         print('3, flee')
#         # print("> ", end=' ')
#         I = input()

#         if I == '1':
#             print('3, flee')
#             #print(goblin1.name)
#             # hero1.attack(goblin1)
#         elif I == '2':
#             pass
#         elif I == '3':
#             print('Bye')
#             break
#         else:
#             print('Invalid input {}'.format(I))
#         if globlin1.health > 0:
#             goblin1.attack(hreo1)

# main()











    class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = 'Generic'

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        print("{} does {} damage to the {}.".format(self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print("{} is dead.".format(enemy.name))
        if self.health <= 0:
            print("{} is dead.".format(self.name))
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))
                  


class Hero(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Hero"


        

class Goblin(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Goblin"


def main():
    hero1 = Hero(10,5)
    goblin1 = Goblin(6,2)

    

    while goblin1.alive() and hero1.alive():
        hero1.print_status()
        goblin1.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero1.attack(goblin1)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin1.health > 0:
            goblin1.attack(hero1)
 

main()