print('输入2个数，做除法。')
print("按'q'退出。")

while True:
    first_num=input('请输入第一个数：')
    if first_num =='q':
        print('你输入了q，程序结束')
        break
    sec_num=input('请输入第二个数：')
    if sec_num=='q':
        print('你输入了q，程序结束')
        break
    try:
        result=int(first_num)/int(sec_num)
    except ZeroDivisionError:
        print('不能除0')
    except ValueError:
        print('输入不是整数')
    else:
        print(f'结果是{result}')