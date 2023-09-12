def hello(name,color,what):
    #geza, kek az eg
    #v8=(c);
    #print(%s, %s ay %s!\n", name, color, what);
    print("{0}, {1} az {2}".format(name, color, what))
    print("{n}, {c} az {o}".format(n=name, c=color, o=what))
    print(f"1+1={1+1}")
    print(f"{name},{color} az {what}")
    print("{n}, {c} az {o}".format(n=name.capitalize(), c=color, o=what)) 
    
def main():
    hello("geza","kek","eg")
if __name__=="__main__":
    main()