#!/usr/bin/env python3

def main():
    
    d={}
    d[2]= [2, 5, 7]
    d[8]= [6, 9, 2]
    d[3]= [8, 6, 5]
    n=9
    #n=3
    for i in d.get(n,[]):
        print(i)
        
    print(d.keys())    
    print(d.values())
        
if __name__=="__main__":
    main()