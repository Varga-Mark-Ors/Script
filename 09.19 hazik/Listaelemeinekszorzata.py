#!/usr/bin/env python3

def product(numbers):
    osszeg = 1
    
    for i in numbers:
        osszeg = osszeg * i
    
    return osszeg

def main():
    #numbers = [1, 2, 3, 4, 5]
    numbers = []
    print("Számok szorzata=",product(numbers))

if __name__=="__main__":
    main()