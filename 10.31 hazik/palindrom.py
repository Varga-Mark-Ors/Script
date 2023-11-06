#!/usr/bin/env python3

def palindrom2(a : int) -> bool:
    a = str(a)
    return a == a[::-1]

def prim(a : int) -> bool:
    if a == 1:
        return False
    else:
        for i in range(2, a // 2):
            if a % i == 0:
                return False
    return True

def palindrom1(a : int) -> int:
     
    while not (palindrom2(a) and prim(a)):
        a += 1
        
    return a

def main():
    print(palindrom1(31))    # 101 
    print(palindrom1(130))   # 131 
    print(palindrom1(131))   # 131 
    print(palindrom1(1977))  # 2002 

if __name__ == "__main__":
    main()