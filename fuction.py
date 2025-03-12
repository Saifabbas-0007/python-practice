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
