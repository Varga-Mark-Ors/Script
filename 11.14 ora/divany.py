#!/usr/bin/env python3

import time
import requests
import urllib.request 

def main():
    url = "https://divany.hu/offline/2017/03/19/urban_outfitters_trendek_felsoresz/?allowed=false#ertekeles_cont_3825927"
    for i in range(50):
        r = requests.get(url)
        html = r.text
        time.sleep(2)
        print("------", flush=True)
if __name__ == "__main__":
    main()