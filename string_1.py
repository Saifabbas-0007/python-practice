name_1 = 'saif'

name_2 = "abbas"

name_3 = """ this is multi line comments """

print(name_1,name_2,name_3) 
"""
string -immutable
follows indexing
p 0
y 1 
t 2
h 3
o 4
n 5
iterable also 

"""
a = "python"
print( a[-1])
'''
+ve indexing starts from 0
-ve indexing starts from -1 

'''
language = "python"
for i in language:
    print(i)

#len function - return the integer value also counts the space 
str = "python is simple language"
print(len(str))

password = "123@#$"
if len(password) >5:
    print("login successful")
else:
    print("login unsuccessful")
    
#____________________
#slicing 
'''
string[start:stop:step]
start = 0
stop = exclusive 
step = gap

'''
text = "pythoniskingofAi"
print(text[1:10:2]) 
text = "pythoniskingofAi"
print(text[::])
text = "pythoniskingofAi"
print(text[::-1])
#repeating a string
number = "20"
print( number *10 )
#__________________
#concatenate adding two string
name = "saif"
ser_name = "abbas"
print (name +  ser_name)

#___________
#checking memnership - in , not in 
text = "python is the king if ai"
print("king" in text)
print("java" not in text) 

email = "@usergmail.com"
if "@" in email:
    print('vald email')
else:
    print("in_valid enail")
str = "THIS IS PYTHON".lower() #lower() case
print( str)
print(str.lower())  
str = input("enter your name").lower()
print(str)
#same with upper case
#________
#capitalise() = omly first character of letter is going to be upper 
str = input ("enter your name").capitalize()
print(str)
 
 #_________
 #title() = basically all the first word if sentence is going to be upper

text = " the python is the king of aiml ".title()
print(text)

#_______
#swapcases() = change the cases upper to lower ,lower to upper

text = input("enter the word").swapcase()
print(text)

#_________
'''
searching and replacing
two types 1- find(pass substring) return the first occurence of the substring
2- replace method 
'''

text = "python programming"
print(text.find("t"))
text = "python programming"
print(text.replace("python","java")) 

#______-
""" 
  spliting  provides list in output  & joining 

"""
text = "a,b,c"
print(text.split(","))

text = "a,b,c"
s = text.split(",")
print("after spliting",s)
result = "," .join(s)
print(result)

#checking method startswith() return boolean  
#sames as endswith()
text = "Python "
print(text.startswith("P")) 
#isalpha = sare word alphabet me hai ?
text = "python programmng"
print(text.isalpha())
#similar with isdigit()
#isalanum
text = "123python"
print(text.isalnum())