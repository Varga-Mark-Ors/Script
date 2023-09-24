#!/usr/bin/env python3

def iterativ(s):
    i = 0
    while i<len(s):
        if(s[i] != s[-(i+1)]):
            print("Nem palindrom")
            break
        
        else:
            i+=1

    if i == len(s) :
        print("Palindrom")


def main():
    s = "gorog"
    
    iterativ(s)

if __name__ == "__main__":
    main()