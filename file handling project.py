#file handling project
import os
print("file handling-mini project")
while True:
    def call():
         print("1. create a file")
         print("2. read the file")
         print("3. write the file")
         print("4. list the file")
         print("5. delete the file")
         print("6. stop the program")
    a=input("choose your option:")
    match a:
        case "1":
            print("CREATING FILE")
            file=input("enter the file name:")
            file=file+".txt"
            print(file)
            filename=open(file,"w")
            print('___________________________________________')
            print("file created successfully",file)
            print('___________________________________________')
            call()
        case "2":
            file=input("enter the file name again:")
            with open(file+'.txt','r') as file:
                file=file.read()
            print('___________________________________________')
            print("file read successfully")
            print('___________________________________________')
            call()
        case "3":
            file=input("enter the file name again:")
            with open(file+'.txt','a')as file:
                con=input('enter the content to be added   ')
                file.write(con)
                print('_______________________________________')
            print("entered content is written successfully")
            print('___________________________________________')
            call()
        case "4":
            print('LISTING FILES')
            path='d:\sree 1st bca'
            listf=os.listdir(path)
            for listf in listf:
                print(listf)
            print('____________________________________________')
            print('listing completed')
            print('____________________________________________')
            call()
        case "5":
            print("removing the file")
            file=input("enter the file name atlast once:")
            path='d:\sree 1st bca'
            file=os.remove(file+'.txt')
            print('______________________________________________')
            print("file deleted")
            print('______________________________________________')
            call()
        case "6":
            print("program end")
            break        
print("**************************")
                           
        
            
            
        
            
        
