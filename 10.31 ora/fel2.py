
import random

def shuffled(li):
    li2=li[:]
    random.shuffle(li2)
    return li2

def main():
    
    li=[1,2,3,4,5]
    print(random.randint(0, 100))
    print(random.random())
    print(random.randrange(0, 100))
    #print(random.shuffle(li))
    print(shuffled(li)[3])
    li = shuffled(li)
    print(li)
    print(random.choice(li))
    
if __name__=="__main__":
    main()