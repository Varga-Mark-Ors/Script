#!/usr/bin/env python3

def main():
    
    ossz=0
    with open("818.txt","r") as f:
        
        for line in f:
            line= line.strip("\n")
            ossz += int(line)      
        
    print(str(ossz)[0:10])
    
if __name__=="__main__":
    main()