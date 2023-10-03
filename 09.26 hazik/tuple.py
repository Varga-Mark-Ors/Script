#!/usr/bin/env python3

import math


def distance(p1, p2):
    a=p1[1]**2+p1[0]**2
    b=p2[1]**2+p2[0]**2
    osszeg=math.sqrt((p2[1]-p1[1])**2 + (p1[0]-p2[0])**2)
    #osszeg=math.sqrt(a+b)
    return osszeg


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()