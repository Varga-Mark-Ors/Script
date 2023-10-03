#!/usr/bin/env python3

mely = list('aáoóuú')
magas = list('eéiíöőüű')

def hang(s):
    me = 0
    ma = 0
        
    for j in mely:
        if j in s:
            me = me + 1
                
    for j in magas:
        if j in s:
            ma = ma + 1
    
    if (ma == 0) and (me > 0):
        return "mely"
    elif (ma > 0) and (me == 0):
        return "magas"
    elif (ma > 0) and (me > 0):
        return "vegyes"
    else:
        return "hangrendetlen"
        

def main():

    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "HHH"]
    
    for i in words:
       h=hang(i)
       print(i,", az ",h)
            
if __name__=="__main__":
    main()