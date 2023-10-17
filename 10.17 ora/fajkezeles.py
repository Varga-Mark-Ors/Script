#!/usr/bin/env python3

def main():
    
    with open("string1.py","r") as f, open("clean_string1.py", "w") as f2:
        
        for line in f:
            if not line.startswith("#"):
                f2.write(line)             
    
if __name__=="__main__":
    main()