
def hamingtav(s1 : str, s2 : str) -> str :
    
    ossz = 0
    if (len(s1) != len(s2)):
        #return "A ket szonak nincs Haming tavolsaga."
        return ossz
    
    else:
        l1 = s1[:]
        l2 = s2[:]
        for i in range(len(l1)):
            if (l1[i] != l2[i]):
                ossz += 1
    
   # return (f"{ossz} a Haming távolsága a 2 szónak.")
    return ossz    

def main():
    
    s1 = "toned" 
    s2 = "rosed"
    #s2 = "rose"

    #print(hamingtav(s1, s2))
    eredmeny = hamingtav(s1,s2)
    
    if eredmeny == 0 :
        print("A ket szonak nincs Haming tavolsaga.")
    else:
        print(f"{eredmeny} a Haming távolsága a 2 szónak.")
#####

if __name__ == "__main__":
    main()