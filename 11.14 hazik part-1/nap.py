#!/usr/bin/env python3

import urllib.request 

def nap(j : str) -> None:
    if j.find("j") > -1:
            if (j.find("s") > j.find("j") and j.find("s") > -1):
                if (j.find("u") > j.find("s") and j.find("u") > -1):
                    if (j.find("n") > j.find("u") and j.find("n") > -1):
                        print(j)

def main():
    url = "https://raw.githubusercontent.com/jabbalaci/Programozas_1/main/datasets/DT2.csv"
    response = urllib.request.urlopen(url)
    raw = response.read()
    html = raw.decode("utf-8")
    #print(type(raw))
    s = html.split("\n")
    #print(s)
    for i in s :
        j = i.lower()
        #print(j)
        nap(j)

    #print(html)
if __name__ == "__main__":
    main()