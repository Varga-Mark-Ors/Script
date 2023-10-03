#!/usr/bin/env python3

import sys
import random as r

UPTO = 100


def main():
    
    db=0
    
    for i in range(UPTO):    
        print(r.randint(0, 9), end="")
        db = db + 1
        if db == 10:
            print()
            db = 0
            
    print()
                
if __name__=="__main__":
    main()