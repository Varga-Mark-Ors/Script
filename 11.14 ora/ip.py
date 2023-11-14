import json
import urllib.request 

def main():
    url = "https://api.ipify.org/?format=json"
    response = urllib.request.urlopen(url)
    raw = response.read()
    html = raw.decode("utf-8")
    f = open ("ip.json", "w")
    json.dump(html,f)
    f2 = open ("ip.json","r")
    d = json.loads(f2)
    print(d["ip"])
    #print(html)
if __name__ == "__main__":
    main()