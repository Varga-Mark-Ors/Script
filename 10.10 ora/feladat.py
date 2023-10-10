#!/usr/bin/env python3

def main():
    
    li=["alma", "narancs", "banan", "alma", "ananasz", "banan"]
    ham=sorted(set(li))
    print(ham) 
    
    b=set()
    b.add(4)
    b.add(9)
    b.add(13)
    print(b)
    b.remove(9)
    print(b)
            
if __name__=="__main__":
    main()