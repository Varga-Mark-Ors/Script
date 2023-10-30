

def main():
    
    ossz = 0
    with open("day02.txt", "r") as f:
        for line in f:
            t = line.split()
            min = 10000000
            max = min * -1
            #print(t)
            for i in t:
                i = int(i)
                if min > i:
                    min = i
                if max < i:
                    max = i
            ossz += (max - min)
            
    print(ossz)
    
    
if __name__=="__main__":
    main()