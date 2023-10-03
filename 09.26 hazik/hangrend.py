#!/usr/bin/env python3

def main():

    mely = list('aáoóuú')
    magas = list('eéiíöőüű')
    words = ["ablak", "erkély", "kisvasút", "magas", "mély"]
    
    for i in words:
        me = 0
        ma = 0
        
        for j in mely:
            if j in i:
                me = me + 1
                
        for j in magas:
            if j in i:
                ma = ma + 1
    
        if (ma == 0) and (me > 0):
            print(i,", az mély szó.")
        elif (ma > 0) and (me == 0):
            print(i,", az magas szó.")
        else:
            print(i,", az vegyes szó.")
            
if __name__=="__main__":
    main()