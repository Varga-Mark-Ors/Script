#!/usr/bin/env python3

import json
import urllib.request

def download_json(url):
    response = urllib.request.urlopen(url)
    raw = response.read()
    html = raw.decode("utf-8")
    return json.loads(html)

def extract_urls(json_data):
    children = json_data['data']['children']
    for child in children:
        url = child['data']['url']
        print(url)

def main():
    json_url = "http://www.reddit.com/r/earthporn/.json"
    json_data = download_json(json_url)

    if json_data:
        extract_urls(json_data)

if __name__ == "__main__":
    main()
