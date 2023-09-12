#!/usr/bin/env python3

def main():
    r=input("Szo=")
    if r[:]==r[: :-1]:
        print("A szo palindrom!")
    else:
        print("A szo nem palindrom!")
if __name__=="__main__":
    main()