# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return
import random
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ssq_red=list(range(1,34))
    ssq_blue=list(range(1,17))
    s_ssq_blue=random.choice(ssq_blue)
    s_ssq_red=[]
    for i in range(6):
        tmp_red=random.choice(ssq_red)
        s_ssq_red.append(tmp_red)
        ssq_red.remove(tmp_red)
    print('红色球：',sorted(s_ssq_red),'蓝色球：',s_ssq_blue)
print_hi('爱我吗，宝宝')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import math

print(math.sin(3.1415926))
for i in range(100):
    print(i)
    try:
        raise ValueError('fefef')
    except ValueError as e:
        print(repr(e))

