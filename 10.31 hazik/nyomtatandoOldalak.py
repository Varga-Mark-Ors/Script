#!/usr/bin/env python3

def oldalak(s : str) -> list:
    l1 = s.split(",")
    l2 = []
    for i in l1 :
        if "-" in i :
            k = i.split("-")
            #print(k)
            a = list(range(int(k[0]), int(k[1]) + 1))
            for j in a : 
                l2.append(j)   
                
        else:
            l2.append(int(i))
    
    return l2    

def rendez(l : list) -> list:
    
    szet = set(l)
    l = list(szet)
    l.sort()
    return l

def main():
    
    s = "1-4,7,9,11-15,14-16,11-20"
    li = oldalak(s)
    li = rendez(li)
    print(li)
    
##############################################################################

if __name__ == "__main__":
    main()
