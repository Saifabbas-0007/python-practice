#append : add the elements in the last of the list
 
a = [1,2,3]
a.append(4)
print(a)

#extend : 
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

#insert method: insert elements where you want without removing or deleting the elements 

list_1 = [1,2,3,4]
list_1.insert(3,"hello coder")
print(list_1) 

#remove method :to delete the particular elments

a = [1,2,3,4]
a.remove(3)
print(a)