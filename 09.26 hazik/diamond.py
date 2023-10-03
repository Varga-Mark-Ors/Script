#!/usr/bin/env python3

def main():
    
    x = int(input("Milyen magas legyen="))
    if (x % 2) == 0:
        print("Az adott szam nem megfelelo!!")
    else:
        d = x // 2
        b = d
        a = 1
        while d >= 0:
            for i in range(d):
               print(" ", end="")
            for i in range(b - d + a):
                print("*", end="")
            print()
            d = d - 1
            a = a + 1  
        a = a - 2 
        d = d + 2 
        while d <= b:
            for i in range(d):
               print(" ", end="")
            for i in range(b-d+a):
                print("*", end="")
            print()
            d = d + 1
            a = a - 1 
            
if __name__=="__main__":
    main()