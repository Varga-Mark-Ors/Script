#!/usr/bin/env python3

def palindromint(a : int) -> bool:
    a = str(a)
    #print(a)
    return a == a[::-1]

def palindromdec(a : int) -> bool:
    a = str(a)
    a = a[2:]
    #print(a)
    return a == a[::-1]

def palindrom1(a : int) -> int:
     
    b = bin(a)
    
    if (palindromint(a) and palindromdec(b)):
        return True
    
    return False

def main():
    ossz = 0
    for i in range(0, 1000000):
        if palindrom1(i):
            ossz += i
            
    print(ossz)

if __name__ == "__main__":
    main()