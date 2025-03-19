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
            