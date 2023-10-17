#!/usr/bin/env python3

from timeit import default_timer as timer

def main():
    start = timer()
    Munchausen = []
    #for i in range(438579089):
    for i in range(10000):
        n = i
        ossz = 0
        #print(i)
        while n != 0:
            p = n % 10
            if p != 0:
                ossz = ossz + (p ** p)
            n = n // 10
        if i == ossz:
            Munchausen.append(i)
            #print(i)
            

    for i in Munchausen:
        print(i) 
        
    end = timer()
    print(end - start)

if __name__=="__main__":
    main()