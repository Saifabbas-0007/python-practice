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
def greet(name , city):
    print(f'hello {name} welcome to the {city}')
greet("saif","noida")
