import Lista1

def main():
    print(Lista1.match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    print(Lista1.match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)

    print(Lista1.front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    print(Lista1.front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])

if __name__ == '__main__':
    main()