import random

def lotto():
    szor = 0
    ossz = 0
    while (ossz != 90) and (szor != 996300) :
        sz1 = random.randint(1,45)
        sz2 = random.randint(1,45)
        sz3 = random.randint(1,45)
        sz4 = random.randint(1,45)
        sz5 = random.randint(1,45)
        sz6 = random.randint(1,45)
        ossz = sz1 + sz2 + sz3 + sz4 + sz5 + sz6
        szor = sz1 * sz2 * sz3 * sz4 * sz5 * sz6
        #print(sz1,sz2,sz3,sz4,sz5,sz6)
    
    print(sz1,sz2,sz3,sz4,sz5,sz6)
    
def main():

    lotto()
#####

if __name__ == "__main__":
    main()