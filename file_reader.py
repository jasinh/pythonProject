filename = r'hello\whyLikeProgramming.txt'
while True:
    i=input('请输入，为什么喜欢编程：')
    if i =='q':
        break
    else:
        with open(filename,'a') as fileobject:
            fileobject.write(f'\n{i}')

with open(filename, 'r') as fileobject:
     for line in fileobject.readlines():
        print(line.strip())





