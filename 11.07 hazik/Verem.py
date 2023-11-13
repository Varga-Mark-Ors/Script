class Verem:
    
    def __init__(self : list[int]) -> None:
        self.data = []
        
    def __str__(self : list[int]) -> str:
        return str(f"{self.data}")
    
    def kivesz(self : list[int]) -> int:
        if len(self.data) > 0:
            return self.data.pop()
        else:
            print("A verem ures.")
        
    def meret(self : list[int]) -> int:
        return len(self.data)
    
    def ures(self : list[int]) -> bool:
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def betesz(self : list[int], szam : int) -> None:
        self.data.append(szam)

def main():
    
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)    # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)
    
if __name__=="__main__":
    main()