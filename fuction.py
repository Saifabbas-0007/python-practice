def greet():
    print("hello")
greet()
'''
parameters: placeholder for the value jo ki function ko call krte time pass kroge
arguments: jo value use hogi usko bolenge exmple saif'''

def greet(name): #parameter
    print("hello",name) 
greet("saif") #arguments
greet("abbas")
greet("saru")  

""" types of arguments
1_position arguments
2_default arguments
3_keyword arguments
"""
#positional arguments
def greet(name , city): 
    print(f'hello {name} welcome to the {city}')
greet("saif","noida")

#keywords arguments
def greet(name , city): 
    print(f'hello {name} welcome to the {city}')
greet(name= "abbas",city ="noida")

#default arguments
def greet(name= "saru" , city= "ghaziabad"): 
    print(f'hello {name} welcome to the {city}')
greet() #if you pass the value here then it will run

#return statments 
def full_name (first_name,last_name):
    name =f'{first_name} {last_name}'
    return name
    #print(name)
variale = full_name("saru","saif")
print(variale)

'''
characteristic
function name must be meaninful
mast be small in lenght
avoid global variable
'''
#local variable :whic can be access inside the function
def msg():
    choice = "i love coding"
    print(choice)
msg()   

#global variable :which can be access outside the function
def msg():
    print("inside the function",choice)
choice = "I Love coding"
msg()  

#decorator
'''example burger - function
extra cheese-extra feature
main function > function adding 
without changing the main function code
'''
def my_decorator(func):
    def wrapper():
        print("hello coder")
        func()
        print("hello python coders")
    return wrapper
@my_decorator
def say_hello():
    print("hii")
say_hello()

#generators  :to generate a sequence of value over a time function is used as "yield"
def count_down(num):
    while num >0:
        yield num
        num -= 1
for number in count_down(5):
    print(number)

#lambda function
add_num =lambda a:a+10
print(add_num(10))
