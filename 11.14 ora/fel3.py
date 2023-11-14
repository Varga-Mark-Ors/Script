import urllib.request as uri


def main():
    
    url = "https://phantom-marca.unidadeditorial.es/5350aaa9b894d9295dd4b2638e853616/crop/0x0/2044x1363/resize/660/f/webp/assets/multimedia/imagenes/2023/11/05/16992180271055.jpg"
    response = uri.urlretrieve(url, "Lebron.jpg")
    #raw = response.read()
    return response
    
if __name__ == "__main__":
    main()