#!/usr/bin/env python3

def main():
    
    with open("trukk.txt", "r") as f, open("trukk2.txt", "w") as f2:
        s= ""
        
        for line in f:
            s= s+ ((chr(int(line, 2))))
        
        f2.write(s)
        
if __name__=="__main__":
    main()