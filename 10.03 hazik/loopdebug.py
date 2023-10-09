
def loop(szam, debug = False):
    if debug:
        print("#Ciklus kezdete:")
        for i in range(1, szam + 1):
            print(i, end=" ")
        print()
        print("#Ciklus vége")
    else:
        for i in range(1, szam + 1):
            print(i, end=" ")
        print()
    return 0

def main():
    
    loop(5)
    print()
    loop(5 , debug = True)   

if __name__=="__main__":
    main()