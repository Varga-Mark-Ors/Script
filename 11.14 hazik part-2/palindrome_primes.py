#!/usr/bin/env python3

import json

def palindrom(i: int) -> bool:
    return str(i) == str(i)[::-1]

def main():
    with open('primes.json', 'r') as file:
        primek = json.load(file)
    
    p = [i for i in primek if palindrom(i)]
    
    print("Palindrom primek=", p)
    print("Darabjuk=", len(p))
          

if __name__ == "__main__":
    main()