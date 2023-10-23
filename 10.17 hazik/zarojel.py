#!/usr/bin/env python3

def test(argument):
    a=list(argument)
    b="([{"
    c=")]}"
    igaz=True
    n=len(a)
    for i in range(n):
        if igaz==False:
            break
        if a[i] in b:
            for j in range(i+1,n):
                if a[j] in c:
                    break
                elif a[j] in b:
                    if b.find(a[i]) < b.find(a[j]):
                        igaz=False
                        break
    return igaz

def main():
    
    print(test("((5+3)*2+1)"))# == True
    print(test("{[(3+1)+2]+}")) #== True
    print(test("(3+{1-1)}"))# == False
    print(test("[1+1]+(2*2)-{3/3}"))#== True
    print(test("(({[(((1)-2)+3)-3]/3}-3)"))# == False
        
if __name__=="__main__":
    main()