#!/usr/bin/env python3

class Greetings():
    def __init__(self,name) -> None:  #konstruktor
        self.name= name
        
    def say_hi(self):
        print(f"Hi, {self.name}!")     # print("Hi, {}!".format(self.name))
    
def main():
    
    g = Greetings("Alice")
    g.say_hi()
    
if __name__=="__main__":
    main()