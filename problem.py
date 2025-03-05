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