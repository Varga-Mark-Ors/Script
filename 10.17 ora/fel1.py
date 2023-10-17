#!/usr/bin/env python3

def main():
    
    f = open("olvas.txt", "r")
    
    for line in f:
        #print(line, end="")
        line = line.rstrip("\n")
        #print(line)
        if line.endswith("line."):
            print(line)   
        
    f.close()
    
if __name__=="__main__":
    main()