#list chracteristic
'''
1- ordered
2- mutable
 3- dynamic 
 4- heterogeneous  '''
# 1 ways using sqaure bracket

my_list = [1,2,3,10.56,True,"hello"]
print(my_list)  

#2 ways using  list constructor

my_list = list((1,2,3,45.67, True,"hello"))
print(my_list)

#list comprehension and range 
#update in list
lst = [1, 2, 3, 4, 5]
print(f"before update{lst}")
lst [2] = "hello"
print(f"after uodate{lst}")
 #if you want to update the multiple value use slice
lst = [ 1,2,3,4,"hello"]
lst[ 1:3 ] = 10 ,56
print(lst) 

#concatenate of list

lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9]
result = lst1 + lst2
print(result)