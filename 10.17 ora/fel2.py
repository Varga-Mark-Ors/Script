#!/usr/bin/env python3

def main():
    
    f = open("olvass.txt", "w")
    
    print("Hello", file=f)
    print(3.14, file=f)
    print(True, file=f, end="")
    
    f.write("bb \n")
    f.write("aa")
            
    f.close()
    
if __name__=="__main__":
    main()