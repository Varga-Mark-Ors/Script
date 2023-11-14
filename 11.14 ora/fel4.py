import os
import urllib.request as uri

def main():
    url = "https://www.thespruce.com/thmb/S15sM3N7Zir_xQBGa14Km6gJuCM=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/the-difference-between-trees-and-shrubs-3269804-hero-a4000090f0714f59a8ec6201ad250d90.jpg"
    response = uri.urlopen(url)
    cmd = f"wget {url} -O trees.jpg"
    
    print(cmd)
    os.system(cmd)
if __name__ == "__main__":
    main()