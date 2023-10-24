#!/usr/bin/env python3

class Proba():
    cnt = 0
    
    def __init__(self):
        Proba.cnt += 1
        pass
    
    i = 12345  # osztalyvaltozo
    
    def hello(self):
        print("Hello!")
    
def main():
    
    print(Proba.cnt)
    p1 = Proba()
    p2 = Proba()
    p3 = Proba()
   
    print(Proba.cnt)
    
if __name__=="__main__":
    main()