#!/usr/bin/env python3

def main():
    
    s1 = input("Elso sztring=")
    s2 = input("Masodik sztring=")
    a = 0
    
    if bool(s1):
        a = a + 1
    if bool(s2):
        a = a + 1
    if not bool(s1):
        a = a - 1
    if not bool(s2):
        a = a - 1
    
    if a == 0:
        print("Igaz az XOR allitas")
    else:
        print("Nem igaz az XOR allitas")
        
if __name__=="__main__":
    main()