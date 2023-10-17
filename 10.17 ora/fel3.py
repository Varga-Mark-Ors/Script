#!/usr/bin/env python3

input= open("be.txt", "r")
output= open("ki.txt", "w")

def main():
    
    for line in input:
        output.write(line)  #== shutil copy (input, output)
    
    input.close()
    output.close()
    
if __name__=="__main__":
    main()