#!/usr/bin/env python3

def szamossz(a):
    ossz=0
    while a > 0:
        d = a % 10
        a = a // 10
        ossz += d
    
    return ossz

def main():
    
    a = 2 ** 1000
    print(szamossz(a)) 

if __name__=="__main__":
    main()