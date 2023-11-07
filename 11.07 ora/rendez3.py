def oszlop(li):

    return li[1]

def main():

    li=[ [2, 6], [1, 3], [5, 4] ]

    print(sorted(li, key=oszlop))
if __name__=="__main__":
    main()