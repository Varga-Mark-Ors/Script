#!/usr/bin/env python3

def main():
    
    with open("string1.py", "r", encoding="utf-8") as f, open("clean_string1.py", "w") as f2:
        
        for line in f:
            #if not line.startswith("#"):
               # f2.write(line)  
            if line.find("#") == -1:
                f2.write(line)            
    
if __name__=="__main__":
    main()