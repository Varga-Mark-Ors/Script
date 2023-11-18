#!/usr/bin/env python3

import json

def is_prime(sz: int) -> bool:
    if sz < 2:
        return False
    for j in range(2, (sz // 2) + 1):
        if sz % j == 0:
            return False
    return True

def main():
    primes = []
    for i in range(10000):
        if is_prime(i):
            primes.append(i)
    
    with open('primes.json', 'w') as file:
        json.dump(primes, file)
    
    print("Mentve")            

if __name__ == "__main__":
    main()

