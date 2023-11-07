def get_bs(li: list[str]) -> str:
    

def main():
    with open("be.txt", "r") as f1:
        li = []
        for line in f1:
            line=line.replace("\n","")
            line=line.replace('"' ,"")
            line=line.replace(".","")
            li.append(line)
    print(li)
    get_bs(li)
    
if __name__=="__main__":
    main()