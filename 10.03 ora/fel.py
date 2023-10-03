#!/usr/bin/env python3

def greet(name, greetings="Hello, "):
    print(greetings + name + "!")
    
def hello(name, repeat=1, postfix="!"):
    for i in range(repeat):
        print("Hello, " + name + postfix)

def main():
    greet("Mark")
    greet("Mark", greetings="Holá, ")
    greet("Mark", greetings="Buna, ")
    
    hello("Laci")
    hello("Leona", repeat=3)
    hello("Leola", repeat=2, postfix=".")
if __name__=="__main__":
    main()