import numpy as np
import math
def kubus():
    a= float(input('masukan sisi'))
    b= float(input('masukan rusuk'))
    
    print("1. mencari luas permukaan")
    print("2. mencari volume")
    print("3. mencari besar sisi/rusuk")
    option = int(input('enter your choice: '))
    
    if option == 1:
        c= 6*a**2
        
        print(c)
    elif option == 2:
        c= b**3
        
        print(c)
        
    elif option == 3:
        a= float(input(" masukan luas permukaan kubus "))
        b= math.sqrt(a/6)
        print(b)
       
    else:
        print("pilihan tidak valid")
        
def balok():
    a= float(input("masukan panjang balok "))
    b= float(input("masukan lebar balok "))
    c= float(input("masukan tinggi balok "))
    
    print("1. mencari luas permukaan")
    print("2. mencari volume")
    print("3. mencari panjang")
    print("4. mencari lebar")
    print("5. mencari tinggi")
    option = int(input('enter your choice: '))
    
    if option == 1:
         d= 2*a*b+2*a*c+2*b*c
         
         print(d)
    elif option == 2:
         d= a*b*c
         
         print(d)
    elif option == 3:
        print("1. dari volume ")
        print("2. dari luas permukaan")
        choice = int(input("enter your choice"))
        if choice == 1:
             a= float(input("masukan volume "))
             b= float(input("masukan lebar "))
             c= float(input("masukan tinggi "))
             d= a/(b*c)
             print(d)
        elif choice == 2:
             a= float(input("masukan luas permukaan "))
             b= float(input("masukan lebar "))
             c= float(input("masukan tinggi "))            
             d= ((a/2)-(b*c))/(c+b)
             
             print(d)
             
        else:
             print("pilihan tidak valid")
    elif option == 4:
        print("1. dari volume ")
        print("2. dari luas permukaan")
        choice = int(input("enter your choice"))
        if choice == 1:
             a= float(input("masukan volume "))
             b= float(input("masukan panjang "))
             c= float(input("masukan tinggi "))
             d= a/(b*c)
             print(d)
        elif choice == 2:
             a= float(input("masukan luas permukaan "))
             b= float(input("masukan panjang "))
             c= float(input("masukan tinggi "))            
             d= ((a/2)-(b*c))/(c+b)
             
             print(d)
             
        else:
             print("pilihan tidak valid")
    elif option == 5:
        print("1. dari volume ")
        print("2. dari luas permukaan")
        choice = int(input("enter your choice"))
        if choice == 1:
             a= float(input("masukan volume "))
             b= float(input("masukan panjang "))
             c= float(input("masukan lebar "))
             d= a/(b*c)
             print(d)
        elif choice == 2:
             a= float(input("masukan luas permukaan "))
             b= float(input("masukan panjang "))
             c= float(input("masukan lebar "))            
             d= ((a/2)-(b*c))/(c+b)
             
             print(d)
             
        else:
             print("pilihan tidak valid")
        
             
def main():
    print("1. mencari sin cos tan")
    print("2. mencari depan")
    print("3. mencari samping")
    print("4. mencari miring ")
    print("5. kubus")
    print("6. balok")
    option = int(input('Enter your choice: ')) 
    if option == 1:
        menu()
    elif option == 2:
        depan()
    elif option == 3:
        samping()
    elif option == 4:
        miring()
    elif option == 5:
        kubus()
    elif option == 6:
        balok()
    else:
        print("pilihan tidak valid")
 
 
def depan():
    print("1. mencari depan sin")
    print("2. mencari depan tan")
    option =int(input("enter your choice"))
    if option == 1:
        a= float(input("masukan sin: "))
        b= float(input("masukan miring: "))
        
        c= a*b
        
        print(c)
    elif option == 2:
        a= float(input("msaukan tan: "))
        b= float(input("masukan depan: "))
        
        c= a*b
        print(c)
    else:
        print("pilihan tidak valid")
    
def samping():
    print("1. mencari samping cos")
    print("1. mencari samping tan")
  
    option =int(input("enter your choice"))
    if option == 1:
        a= float(input("masukan cos: "))
        b= float(input("masukan miring: "))
        
        c= a*b
        
        print(c)
    elif option == 2:
        a= float(input("msaukan tan: "))
        b= float(input("masukan depan: "))
        
        c= b/a
        print(c)
    else:
        print("pilihan tidak valid")
    
def miring():
    print("1. mencari miring sin")
    print("1. mencari miring cos")
  
    option =int(input("enter your choice"))
    if option == 1:
        a= float(input("masukan sin: "))
        b= float(input("masukan depan: "))
        
        c= b/a
        
        print(c)
    elif option == 2:
        a= float(input("msaukan cos: "))
        b= float(input("masukan samping: "))
        
        c= b/a
        print(c)
    else:
        print("pilihan tidak valid")
     
    
def menu ():
    a= int(input('masukan sisi depan '))
    b= int(input('masukan sisi samping '))
    c= int(input('masukan sisi miring '))

    print("1. sin")
    print("2. cos")
    print("3. Tan")
   
    option = int(input('Enter your choice: ')) 
    if option == 1:
        d= a/c
        e= math.sin(d)
        print(e)
    elif option == 2:
        d= b/c
        e= math.cos(e)
        
        print(e)
    elif option == 3:
        d= a/b
        e= math.tan(d)
        print(e)

    else:
        print('Invalid option. Please enter a number between 1 and 4.')
 
if __name__=="__main__":
    while True:
        main()