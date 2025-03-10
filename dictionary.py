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
