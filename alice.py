filename='alice.txt'
try:
    with open(filename) as fileobject:
        contents=fileobject.read()
except FileNotFoundError:
    print('no found file')
else:
    words=contents.split()
    print(len(words))
    print(f'艾丽斯的字数一共：{len(words)}')
