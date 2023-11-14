import random

def lotto():
    max_kiserlet = 1000000  
    szor = 1
    ossz = 0
    kiserlet = 0
    li = [0, 0, 0, 0, 0, 0]

    while (ossz != 90) and (szor != 996300) and (kiserlet < max_kiserlet) and (len(set(li)) != len(li)):
        szor = 1
        ossz = 0

        for i in range(6):
            li[i] = random.randint(1, 45)
            ossz += li[i]
            szor *= li[i]

    if kiserlet < max_kiserlet:
        print("Nyerőszámok:", end=" ")
        li.sort()
        for i in range(6):
            print(li[i], end=" ")
    else:

import urllib.request 

