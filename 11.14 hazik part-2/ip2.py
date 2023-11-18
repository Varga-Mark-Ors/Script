#!/usr/bin/env python3

from urllib.request import Request, urlopen

def keressip(s : list[str]) -> str:
    for i in s :
        j = i.lower()
        if "\"ip\"" in j:
            return j
        
def formaz(s : str) -> str:
    s = s.replace("{","").replace("}","").replace("\"","")
    s = s[3:]
    return s

def main():
    
    req = Request(url='https://reallyfreegeoip.org/json/', headers={'User-Agent': 'Mozilla/5.0'})
    raw = urlopen(req).read()
    html = raw.decode("utf-8")
    s = html.split(",")
    
    print("Az Ön IP címe:", formaz(keressip(s)))
    
if __name__ == "__main__":
    main()