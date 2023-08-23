import numpy as np
import math

def main():
    print("mencari sin cos tan")
    print("mencari depan")
    print("mencari samping")
    print("mencari miring ")
    option = int(input('Enter your choice: ')) 
    if option == 1:
        menu()
    elif option == 2:
        depan()
    elif option == 3:
        samping()
    elif option == 4:
        miring()
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