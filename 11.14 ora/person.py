import json

def main():
    f = open("person.json", "r")
    f2 = open("person2.json", "w")
    d = json.load(f)
    
    print(d)
    print(type(d))
    print(d['age'])
    print(d['daughter']['age'])
    json.dump(d, f2)
    f.close()
    f2.close()
if __name__ == "__main__":
    main()