def count_words(filename):
    try:
        with open(filename) as fileobject:
            contents=fileobject.read()
    except FileNotFoundError:
        print(f'{filename}文件不存在')
    else:
        print(f'{filename}文件一共：{len(contents.split())}字')

def main():
    books=['alice.txt','pi_digits.txt','fefe.txt']
    for book in books:
        count_words(book)


if __name__== '__main__':
    main()
