
def main():
    
    Munchausen = []
    #for i in range(438579088):
    for i in range(10000):
        n=i
        ossz = 0
        while n != 0:
            p = n % 10
            if p != 0:
                ossz = ossz + ( p ** p)
            n = n // 10
        if i == ossz:
            Munchausen.append(i)

    for i in Munchausen:
        print(i) 

if __name__=="__main__":
    main()