def id(s : str) -> int:
    t = s.split(":")
    s = t[0]
    #print(s)
    return int(s) * -1

def main():
    
    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(sorted(users, key=id))
    
if __name__=="__main__":
    main()