#!/usr/bin/env python3

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

def main():
    
    a = list(TEXT)
    i = 0
    
    
    for i in range(len(a)):
        d = ord(a[i])
        if (d > 96 and d < 121) or (d > 64 and d < 89):
            d = d+2
        
        elif (d == 89) or (d == 90):
            d = d+8
            
        elif (d == 121) or (d == 122):
            d = d - 24
            
        a[i] =chr(d)
            
    
    b=""
    for i in a:
        b = b + i
    print( b )

##############################################################################

if __name__ == "__main__":
    main()