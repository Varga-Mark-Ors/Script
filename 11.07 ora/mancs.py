import sys

def cat(name):
    try:
        f = open(name, "r")
        text = f.read()
        print('---', name)
        print(text)
        f.close()
    except FileNotFoundError:
        print("---- I/O erro:", name)


def main():
    
    args =sys.argv[1:]
    for arg in args:
        cat(arg)
    
if __name__=="__main__":
    main()