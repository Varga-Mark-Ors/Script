import random

def mychoice(li):
    n = len(li)
    return random.randrange(0, n)

def main():
    
    li=[66,44,22,11,65]
    print(li[mychoice(li)])    
    
if __name__=="__main__":
    main()