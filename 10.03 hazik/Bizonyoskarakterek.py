
def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):

    s = ""
    for i in text:
        if i in chars:
            s += i
    return s

def main():
    
    szo=input("Mi legyen a szo?")
    #print(valid(szo, chars="abcdefg"))
    print(valid(szo))

if __name__=="__main__":
    main()