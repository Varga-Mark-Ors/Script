#!/usr/bin/env python3
# coding: utf-8

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A magyar változatot készítette:
# Szathmáry László (jabba.laci@gmail.com)
# frissítés Python 3-ra: 2016.09.09.

# További sztring műveletek


def verbing(s):
    c=s[:]
    if len(s)>2:
        if s[-3:]=="ing":
            c=s[:]+"ly"
        else:
            c=s[:]+"ing"
    return c


def not_bad(s):
    bad=s.find("bad")
    no=s.find("not")
    c=s
    if (no>-1) and (bad>-1):
        if (no<bad):
            c=s[:no]+"good"
    if s[-1]=="!":
        c=c+"!"
    if s[-1]==".":
        c=c+"."
    if s[-1]=="?":
        c=c+"?"
    return c


def front_back(a, b):
    d=(len(a)/2)
    if d!=(d//1):
        d=int(d+1)
    else:
        d=int(d)
    g=(len(b)/2)
    if g!=(g//1):
        g=int(g+1)
    else:
        g=int(g)
    c=a[:d]+b[:g]+a[d:]+b[g:]
    return c


# Egy egyszerű teszt fv. Kiírja az egyes fv.-ek visszaadott értékét, ill.
# azt is, hogy mit kellett volna visszaadniuk.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


# Ezt ne módosítsuk.
# A main() fv. meghívja a fenti fv.-eket különféle paraméterekkel,
# s a test() fv. segítségével megnézi, hogy az eredmények helyesek-e.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

#############################################################################

if __name__ == '__main__':
    main()