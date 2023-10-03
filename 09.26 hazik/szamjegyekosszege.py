#!/usr/bin/env python3

def main():
    
    x = list(range(1,101))
    osszeg = 0
    for i in x :
        while i != 0 :
            a = i % 10
            i = i // 10
            osszeg += a
            
    print(osszeg)
    
if __name__=="__main__":
    main()