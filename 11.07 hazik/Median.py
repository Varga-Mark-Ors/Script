def test(dt : list[int]) -> float:
    dt.sort()
    n= len(dt)
    if n % 2 == 0:
        median = (dt[n // 2] + dt[(n // 2) - 1]) / 2
    else:
        median = dt[n // 2]
    
    return median

def main():
    
    print("Elso teszt=", test([1, 2, 3, 4, 5])) #== 3
    print("Masodik teszt=", test([3, 1, 2, 5, 3])) #== 3
    print("Harmadik teszt=", test([1, 300, 2, 200, 1])) #== 2
    print("Negyedik teszt=", test([3, 6, 20, 99, 10, 15])) #== 12.5

if __name__=="__main__":
    main()