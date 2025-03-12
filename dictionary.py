"""
dictionary {}
characteristic
1- pair = key :value
1 unordered 3.7version, but now it is ordered
3- mutable
4- dynamic
5- key namealways unique 
 """
my_dict ={ 
    "name":"saif","age":23,"marks":62.67,100:"abcd"
}
print(my_dict)
my_dict ={
    "marks":[1,2,3,'saif']
}
print(my_dict)

#adding new value in dict
my_dict ={
    'fruites':['kela','apple','orange'],'categor':'fruites'
} 
print(my_dict)
my_dict['prices'] = 100
print(my_dict)

#updation
my_dict ={
    'name':'saif','language':'python','version':3.9 #if key is same the value is update
}
print(my_dict)
my_dict['version'] = 4.0
print(my_dict) 
my_dict ={
    'name':'saif','language':'python','version':3.9 #if key is diff it add that value  
}
print(my_dict)
my_dict['updated_version'] = 4.0
print(my_dict) 

#deleting the value from dict
my_dict ={
    'name':'saif','language':'python','version':3.9,'use case':['ai','ml','da',]
}
print(my_dict)
del my_dict['version']
print(my_dict) 

#get() method 
my_dict = {
    'name':'saif','age':23,'salary':25000.00
}
age = my_dict.get('age')
print(age)

#keys()
my_dict = {
    'name':'saif','age':23,'salary':25000.00
}
keys = my_dict.keys()
print(list(keys))

#values()
my_dict = {
    'name':'saif','age':23,'salary':25000.00
}
value = my_dict.values()
print(list(value))  

#items(): to call keys and value elements
my_dict = {
    'name':'saif','age':23,'salary':25000.00
}
all_items = my_dict.items()
print(list(all_items))
 
#popped()method
my_dict = {
    'name':'saif','age':23,'salary':25000.00
}
popped = my_dict.pop('age')
print(popped)
print(my_dict)
 
 #popped items():to delete the last elements from the dict
my_dict = {
    'name':'saif','age':23,'salary':25000.00
}
popped_i = my_dict.popitem()
print(popped_i)
print(my_dict)

#clear():to delete the total elements of dict
my_dict = {
    'name':'saif','age':23,'salary':25000.00
}
clear_i = my_dict.clear()
print(my_dict)
print(clear_i)

#dict comprehension 
squares = {a: a *a for a in range(1,6)}
print(squares)

 #nested dict:
programming_language = {
    "python":{"name":"python","versio":4.9,"use_case":[ 'ai,ml,webdev']}
    ,"java":{"name":"java","versio":3.9,"use_case":[ 'ai,ml,webdev']}
}
print(programming_language)

#loops in dict

rogramming_language = {
    "python":{"name":"python","versio":4.9,"use_case":[ 'ai,ml,webdev']}
    ,"java":{"name":"java","versio":3.9,"use_case":[ 'ai,ml,webdev']}
}
for keys in programming_language.keys():#here also use values toget the value of dict or to get all the elements use items()
 print(keys)

