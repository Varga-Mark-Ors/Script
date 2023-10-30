class Sor:
    
    def __init__(self) -> None:
        self.data = []
        
    def __str__(self) -> str:
        return str(f"{self.data}")
    
    def kivesz(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            print("A verem ures.")
        
    def meret(self):
        return len(self.data)
    
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def append(self, szam):
        self.data.append(szam)

def main():
    
    v = Sor()      # üres verem létrehozása
    print(v)         # [
    print(v.is_empty())  # True
    v.append(1)
    v.append(4)
    v.append(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.is_empty())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)    # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)
    
if __name__=="__main__":
    main()