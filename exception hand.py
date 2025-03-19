'''
errors
1- compile time error: we forget the colon(:) in some statements
2- runtime error:
3- logical error
'''
'''
exception
1- starts running
2- warning sing
3- catch and handle
'''
'''
exception handling : handles the errors that are occuring during the execution of program
try - except
try - error code
except - if error occur then what should done 
'''

try:
    number = int(input("enter the numner"))
    result = 10/number
    print(f'result ,{result}')

except ZeroDivisionError:
    print("you cannot divide with zero")

except ValueError:
    print("you cannot divide with string")

'''finally block: execute always even error occur'''   
'''nested try-except'''

try:
    num_1 =int(input('enter the num 1 '))
    num_2 = int(input('enter the num 2 '))
    try:
        result = num_1 / num_2
        print(f'result,{result}')
    except ZeroDivisionError:
        print('you cannot divide with 0')

except ValueError:
    print('you must provide the valid input') 

#check password strength

def check_password(password):
    if len (password)<8:
        raise Exception("Error: Password must be greater the 8 character ")
    print("Password is strong")
try:
    password =input("enter the password = ")
    check_password(password)
except Exception as e :
    print(e)

        