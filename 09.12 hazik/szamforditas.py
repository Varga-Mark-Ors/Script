#!/usr/bin/env python3


def main():
    a=int(input("Szam="))
    b=str(a)
    if b[-1]=="0":
        print('Nem lehetseges a forditas!')
    else:
        b=b[: :-1]
        b=int(b)
        print(b)
if __name__=="__main__":
    main()
