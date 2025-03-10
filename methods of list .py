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

#pop method:same as remoive but in this you have give the index of the elements
# in this example here we give the index no.2 and the return value is element that is 3
a = [1,2,3,4]
popped = a.pop(2)
print(popped)
print(a)
 #clear()method :that clear the total elements of list 
lst =[1,2,3,4,5]
lst.clear()
print(lst)

# index()method :that tells the index of the elements
lst = [1, 2, 3, 4, 5,]
index = lst.index(5)
print(index)

#count() method :that tells how many times the elements is occur 
lst = [1, 2, 3, 4, 1, 1, 3, 1, 1, 'java', 'python','dsa'] 
counter = lst.count("java")
print(counter)

#sort : that aort the elemnts
lst =[24,56,78,90,56,-12,-23,98,89]
lst.sort()
print(lst)

#reverse() method : to reverse the list 
lst = [1, 2, 3, 4]
lst.reverse()
print(lst)
 
#copy() method : to copy the elements of list 
a = [1,2,3,4]
a_copy = a.copy()
print(a_copy) 

#min ,max() method : to find the min and max value from the list
lst = [1,20,300,56,-21]
print(min(lst))
print(max(lst))

#common elements :to find the common elements
lst_1 = [1,2,3,4]
lst_2 = [3,4,5,6]
# now first change this into set to proceed further
s1 = set(lst_1)
s2 = set (lst_2)
s3 = s1.intersection(s2)
print(list(s3))
