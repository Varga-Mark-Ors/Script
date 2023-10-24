#!/usr/bin/env python3

class Bag():
    def __init__(self) -> None:
        self.data = []
        
    def add(self, value):
        self.data.append(value)
        
    def __str__(self) -> str:  #to-string
        #return str(self.data)
        return f"Bag {self.data}"
    
    def add_twice(self, value):
        self.add(value)
        self.add(value)
    
def main():
    
    b = Bag()
    b.add(5)
    b.add(7)
    b.add(18)
    print(b)
    b.add_twice(9)
    print(b)
    
if __name__=="__main__":
    main()