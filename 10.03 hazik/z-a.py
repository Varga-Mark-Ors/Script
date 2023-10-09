
def main():
    
    s=""
    p = [chr(122 - i) for i in range(26)]
    for i in p:
        s+= i
    print(s)

if __name__=="__main__":
    main()