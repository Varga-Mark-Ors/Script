#!/usr/bin/env python3

def alcatraz(li: list[int], i: int) -> list[int]:
    for j in range(i - 1, 600, i):
        if li[j] == 0:
            li[j] = 1
        else:
            li[j] = 0
    return li

def main():
    li = [0] * 600
    for i in range(1, 601):
        li = alcatraz(li, i)

    for i in range(len(li)):
        if li[i] == 1:
            print(i + 1, end="")

if __name__ == "__main__":
    main()

