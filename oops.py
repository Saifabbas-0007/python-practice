warrior_name = "thor"
warrior_health = 100
warrior_attack = 80

mage_name ="gandalf"
mage_attack =100
mage_health =70
def attack_warrior():
    print(f'warrior attack power',warrior_attack)
def attack_mage():
    print(f'mage attack power',mage_attack)
attack_warrior()
attack_mage()

# now this can be write with oops 
class character:
    def __init__(self,name,attack,health):
        self.name = name
        self.attack = attack
        self.health = health

    def attack_enemy(self):
        print(f'{self.name} attack with power {self.attack}')
warrior = character("thor",80,100)
mage = character("gandalf",90,200)
warrior.attack_enemy()
mage.attack_enemy()

"""
1 classes & objects
2 inheritence
3 encapsulation
4 abstraction
5 polymorphism

 """
'''
class - a blue print or template for creating objects
map -class
house - objects '''

class car():
    def detail(self,brand,model):
        self.brand = brand
        self.model = model
    def show_detail(self):
     print(f'this is a car,{self.brand} {self.model}')

car_1 = car()
car_1.detail("bMW","M5")

car_2 =car()
car_2.detail("mercedes","G-wagon") 

car_1.show_detail() 
car_2.show_detail()



       