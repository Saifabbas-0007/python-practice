#control staments 
""" if, elif, else
for while else suited
nested
infinte loop
break
pass 
assert
continue 
"""
age = int (input('enter your age = '))
if ( age>= 18 and age<= 101):
    print('you can vote!')

elif age >= 101:
    print('greater than 101')

elif age <= 0:
    print('invalid age')
    
else:
    print('error occured')

#calculator 
num_1 = float(input('enter the number 1 ='))
num_2 = float(input('enter the number 2 =')) 
choice = input ('enter the choice + - * / // % **')
if choice == '+':
    print(f'addition: {num_1 + num_2}')
elif choice == '-':
    print(f'subtraction: {num_1 - num_2}')
elif choice == '*': 
    print(f'multiplication: {num_1 * num_2}')
elif choice == '/':
     print(f'division: {num_1 * num_2}')
elif choice == '**':
     print(f'exponents: {num_1 * num_2}')
else: 
    print('invalid choice')

"""
loops 
while loop
for loop

"""
i = 1
while i<= 5:
    print(i)
    i +=1
"""
 for loop -
  a =[1,2,3,4,]
  for i in :
  print(i)

 """
#range function 
#range (start,stop,step)
a = tuple(range(1,11,1))
print(a)
for i in range (1,3):
    for j in range (3,6):
        print(f'{i},{j}')

for num in range (1,10,1):
    if num == 5:
        break
    print( num )

    for num in range (1,10,1):
        if num == 4:
            continue #skip
        print( num)

for i in range (1,11):
    if i %2 == 0:
        print('even',i) 
    else: 
        print('odd',i) 
        
        start = int (input('enter the start number'))
        stop = int(input('enter the stop number'))
        skip = int (input('enter the skip number'))
        for i in range (start,stop):
            if i == skip:
                continue
            print(i)