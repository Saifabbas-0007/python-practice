print("hello world")
print("hello world")
# single line comments
''' this is multi line comments'''
""" this is also multi line comments"""
print("hello")
#data types
"""
numeric datatype
float- decimal number 2.3  12.34
int -whole number 100 200 -100 
complex - real +imaginary number 
a+bj
3+4j
"""
a= 10
b= 15.4
c= 3+4j
print(a,b,c)
print(type(a), type(b), type(c))
""" boolean data type
its give true false 
used for logical operations
"""
is_raining= True
is_sunning = False
print(is_raining ,is_sunning)
#none datatype
result = None
print(result)
#sequence datatype
"""
string - immutable "data" 'data' 
list - mutable ,
tuple - immtuable 
 """ 
text = "this is a string"
print(type(text ))
my_list = ['data1','data2','data3',]
print(my_list)
my_tuple = ('data1','data2','data3')
print(my_tuple)
    #set(mutable)
    #frozenset(immutable)
unique_number =  {1,2,3,3,3,4,4,4,4,5,}
print(unique_number)
unique_set = frozenset({1,1,1,2,3,4,4,5,})
print(unique_set)
     #mapping datatype
#dictionary key value pair
person = {
    'name':'gopal','age': 100,'number':1234456774
} 
print(person)
"""
operators 
solution -PEMDAS 
"""
#arithmetic operator
result = 10+5*2
print(result)
x = 10
y = 20
print(x+y)
print(x-y)
print(x*y)
print(x/y) #division
print(x//y)#floor value 
print(x%y) #remainder
print(x**y) #exponents
#comparison operator
#true or false
x = 10
y = 20

print( x == y)
print( x != y)
print( x > y)
print( x < y)
print( x >= y)
print( x <= y)
""" logical operator
can be used to perform multiple line condition  boolean answer 
and 
or
not """

age = 20
is_student = True
print( age>18 and is_student)
print( age>25 or is_student)
print( not is_student)
""" assignment operator
=
+=
-=
*=
"""
x = 10
x += 5
print(x)
""" identity operator - to compare the memory location of two objects
is -return true if same memory location
is not - return true if memory location is not same """
a =[1,2,3]
b = a
c =[1,2,3]
print( a is b)
print( a is c)
""" membership operator - to check whetgher the value is exit in sequence or not
in - 
not in -
"""
vegetables =['karela','aloo', 'tamatar']
print('karela' in vegetables)
a = 2
a += 2
b = a
print(a,b)
