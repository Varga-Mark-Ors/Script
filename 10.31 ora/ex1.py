
import pygyak

def main():
    
    list = []
    for i in range(100):
        if pygyak.is_prime(i):
            list.append(i)
    print(list)
    
    print(pygyak.helloworld())
    
if __name__=="__main__":
    main()