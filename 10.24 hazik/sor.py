from collections import deque

class Sor:
    
    def __init__(self) -> None:
        self.data = deque([])
        
    def __str__(self) -> str:
        return str(f"{self.data}")
    
    def kivesz(self):
        if len(self.data) > 0 :
            return self.data.popleft()
        else:
            print("A verem ures.")
        
    def meret(self):
        return len(self.data)
    
    def ures(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def betesz(self, szam):
       # if len(self.data) == 0:
            self.data.append(szam)
            
        #else:
           # self.data.append(szam)
           # cs = self.data[len(self.data) - 1]
           ###     self.data[i] = self.data[i - 1]
           # self.data[0] = cs
def main():
    
    v = Sor()      # üres verem létrehozása
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