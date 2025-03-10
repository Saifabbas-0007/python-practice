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

#repeated 
lst = [1, 2, 3, "python"]
print(lst *5)

#membership to check that the element is presents in lst or not
# in ,not in

lst = [1, 2, 3, 4, 5]
check = int (input ("enter the  number to check"))
if check in lst :
    print("found")
else:
    print("not found")

#alias - copy of data
list_1 = [1,2,3]
list_2 = list_1
list_2[0] = 100
print(list_2) #here the changes occur in both the list

#to overcome this the concept of copy() method is present

list_1 = [1,2,3]
list_2 = list_1.copy()
list_2[0] = 100
print( list_1 ,list_2)

