import pygyak #from pygyak import is_prime, helloworld

def main():
    
    ossz = 0
    for i in range(200):
        if pygyak.is_prime(i):
            ossz += i
    print(ossz)
    
if __name__=="__main__":
    main()