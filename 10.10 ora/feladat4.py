#!/usr/bin/env python3

def main():
    
    d={}
    print(type(d))
    d["a"]="alfa"
    d["v"]="vareszy"
    d["b"]="beta"
    d["g"]="giga" 
    d["d"]="delta"
    
    for k in sorted(d.keys()):
        print(k, "----->", d[k])   
if __name__=="__main__":
    main()