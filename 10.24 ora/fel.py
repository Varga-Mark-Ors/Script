#!/usr/bin/env python3

class EmptyClass:
    pass

class MyClass:
    def hello(self):
        print("Hello, world!")
        
def main():
    
    o = EmptyClass()
    o = MyClass()
    o.hello() #= o.hello(o)
    
    
if __name__=="__main__":
    main()