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

#self : is a keyword that is used inside the class to refer to the current objects
'''class students():
    def set_details(name ,age)
        name = name 
        age = age
students1 =students()
students1.set_details("saif",90)
print(students1.name)
'''
class students():
    def set_details(self,name ,marks):
        self.name = name 
        self.marks = marks
students1 =students()
students1.set_details("saif",90)
print(students1.name,students1.marks)

#constructor :__init__()
#without constructor

class car():
    def set_details(self,name,color):
        self.name = name
        self.color = color
car1 = car()
car1.set_details('bmw','red')
print(car1.name)
print(car1.color)

#with constructor

class car():
    def __init__(self,name,color):
        self.name = name
        self.color = color
car1 = car('bmw','black')
print(car1.name,car1.color)

class students :
    def __init__(self,name ,age , grade):
        self.name = name
        self.age = age
        self.grade = grade
students1 = students('saif',23,'A+') 
students2 = students('saru',20, 'A+') 
print(students1.name,students1.age,students1.grade)
print(students2.name,students2.age,students2.grade)

'''
types of constructor
1- default constr
2-parameterized constr(self, age, name)
constr with default value(self, name = "unknown)'''

"""
polymorphism
one name , many form
same function name alg alg datatypes ke leye kaam karega 
same methods name alg alg classes ke leye alg alg kaam karega
example run
1- a person can run fast
2- car runs on petrol
 """
print(len("python"))
print(len((1,2,3)))
print(len({"a":1,"b":2,"c":3}))

#method overriding
class bird():
    def sound(self):
        print("bird make sound")
class crow(bird):
    def sound(self):
        print("crow sounds caw caw")
class parrot(bird):
    def sound(self):
        print("parrot sounds squawk")
bird1 = crow()
bird2 = parrot( )
bird1.sound()
bird2.sound()

print(10+5)
print("hello"+"saif")
print([1,2,3]+[4,5])

'''
encapsulation
hiding the internal details of objects '''

class Bankaccount():
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance #to make he balance private
    def deposit(self,amount):
        self.__balance += amount
        print(f'deposited{amount}.new balance{self.__balance}')
    def get_balance(self):
        return self.__balance #controlled access
account = Bankaccount("12345",5000)

account.deposit(2000)
print(account.get_balance)

'''
inheritence
to use the property of parent class in the child class
'''

class Animal():
    def speaks(self):
        print("animals make sound")

class Dog (Animal):
    def bark(self):
        print("dog barks") 
dog= Dog()              
dog.bark()
dog.speaks()

'''
abstarction
complex  implementation deatils ko hide karna aur bs zarori details show karna user ko
 '''           
from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start (self):
        pass 
class car (vehicle):
    def start(self):
        print("car starts with a key")

class bike(vehicle):
    def start(self):
        print("bike starts with a butt0n")

car = car()
bike =bike() 
car.start()
bike.start()

