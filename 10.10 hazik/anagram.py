#!/usr/bin/env python3

def normalize(s):
    s=s.replace(" ","")
    s=s.lower()
    return s

def szamanag(s):
    sz = dict([(chr(i),0) for i in range(97,123)])
    for i in s:
        sz[i] += 1
    return sz

def anagram(s1, s2):
    sz1 = szamanag(s1)
    sz2 = szamanag(s2)
    if sz1 == sz2:
        print("Anagram")
    else:
        print("Nem anagram")

def main():
    
    a = "Clint Eastwood"
    a = normalize(a)
    
    b = "Old west action"
    #b = "Old west actions"
    b = normalize(b)
    
    anagram(list(a), list(b))

if __name__=="__main__":
    main()