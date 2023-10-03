#!/usr/bin/env python3

def main():
    
    a = list(range(1,101))
    osszega = sum(a) ** 2
    osszegb = 0
    
    for i in range(1,101):
        osszegb=osszegb + (i ** 2)
    
    print(osszega - osszegb)    
if __name__=="__main__":
    main()