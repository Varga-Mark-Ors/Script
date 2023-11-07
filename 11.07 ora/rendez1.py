def my(t):
    return t[-1]

def main():
    data = [ 
    (1, 'Albany', 'NY', 162692),
    (3, 'Allegany', 'NY', 11986),
    (121, 'Wyoming', 'NY', 8722),
    (123, 'Yates', 'NY', 5094)
]
    
    print(sorted(data, key=my))
    print(sorted(data, key=lambda t : t[-1]))

    
if __name__=="__main__":
    main()