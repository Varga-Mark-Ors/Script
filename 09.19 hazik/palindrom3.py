#!/usr/bin/env python3

def rekurz(s):
    if s == "":
        print("Palindrom")
        return 0
    if s[0] == s[-1]:
        rekurz(s[1:-1])
    else:
        print("Nem palindrom")
        return 0

def main():
    s = "gorog"
    
    rekurz(s)

if __name__ == "__main__":
    main()