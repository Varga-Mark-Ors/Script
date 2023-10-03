#!/usr/bin/env python3

def mysorted(li):
    n = len(li)
    newli = li
    igaz=False
    for i in range(0,n-1):
        for j in range(1,n):
            if newli[i]>=newli[j]:
                cs=newli[i]
                newli[i]=newli[j]
                newli[j]=cs
                
    return newli

def main():
    
    li=[7,4,2,9,10]
    
    mysorted(li)
    print(li)
            
if __name__=="__main__":
    main()