

def main():
        i=438579088
        n=i
        ossz = 0
        while n != 0:
            p = n % 10
            if p!=0:
                ossz = ossz + ( p ** p)
            #print(p**p)
            n = n // 10
        #print(ossz)
        if i == ossz:
            print("Munch")
              
if __name__=="__main__":
    main()