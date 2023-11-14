import urllib.request

def get_page(s):
    url = s
    response = urllib.request.urlopen(url)
    raw = response.read()
    html = raw.decode("utf-8")
    s = html
    return s
    #print(html)
