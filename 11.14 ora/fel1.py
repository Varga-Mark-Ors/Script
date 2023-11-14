
import urllib.request 

def main():
    url = "https://www.python.org/"
    response = urllib.request.urlopen(url)
    raw = response.read()
    html = raw.decode("utf-8")
    print(type(raw))
    print(type(html))
    #print(html)
if __name__ == "__main__":
    main()