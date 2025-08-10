"""
#write method
file = open('sample.txt','w')
file.write("hello ji! this is python")

#read method
file = open('sample.txt','r')
content = file.read()
file.close()
print(f"content of 'sample.txt',{content}") 

"""
import os
def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"file Name{filename}:created successfully!")
    except FileExistsError:
        print(f"file Name{filename} already occured!")
    except Exception as E:
        print("An error occured")

def view_all_files():
    files = os.listdir()
    if not files:
        print(" No File Found!")
    else:
        print(" files in diectory!")
        for file in files:
            print(file)

def delete_file_(filename):
    try:
        os.remove(filename)
        print(f"{filename} deleted successfully!")
    except FileNotFoundError:
        print('file not found!')
    except Exception as E:
        print("An error occured!")

def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content = f.read()
            print(f"content of '{filename}' : \n {content}")
    except FileNotFoundError:
        print('file not found!')
    except Exception as E:
        print("An error occured!")

def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content = input("enter the data to be add = ")
            f.write(content +"\n")
            print("content added to {filename} successfully!")
    except FileNotFoundError:
        print('file not found!')
    except Exception as E:
        print("An error occured!")

def main():
    while True:
        print(" FILE MANAGEMENT APP")
        print('1: create file')
        print('2: view all file')
        print('3: delete file')
        print('4: read file')
        print('5: edit file')
        print('6: Exit')

        choice = input('enter your choice(1-6) = ')
        if choice == '1':
            filename = input('enter the fie-name to created = ')
            create_file(filename)

        elif choice =='2':
            view_all_files()

        elif choice == '3':
            filename = input('enter the file name you want to delete = ')
            delete_file_(filename) 

        elif choice == '4':
            filename = input('enter the file name you want to read = ')
            read_file(filename)

        elif choice == '5':
            filename = input('enter file name to edit = ') 
            edit_file(filename)      

        elif choice == '6':
            print('closing the app...')
            break
        else:
            print('In-valid Number')

if __name__ =="__main__":
    main()
    







        

