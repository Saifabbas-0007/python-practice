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
