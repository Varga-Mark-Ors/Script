
import urllib.request 

def main():
    url = "https://raw.githubusercontent.com/jabbalaci/Programozas_1/main/datasets/DT2.csv"
    response = urllib.request.urlopen(url)
    raw = response.read()
    html = raw.decode("utf-8")
    print(type(raw))
    
    s = html.split()
    #print(s)
    for i in s :
        j = list(i.lowercase())
        if (j,s,u,n) in j :
            print(i)
    #print(html)
if __name__ == "__main__":
    main()