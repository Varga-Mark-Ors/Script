#!/usr/bin/env python3

class Hello:
    
    def display_name(self):
        return self.name
    
    def create_name(self,name):
        self.name = name
        
    def greet(self):
        print("Hello,", self.name, "!")
        
def main():
    
    h = Hello()
    h.create_name("Alice")
    print(h.display_name())
    
    h.greet()
    
if __name__=="__main__":
    main()