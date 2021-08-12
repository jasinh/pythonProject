import json
def greet_user():
    print('如果以前存储了用户名，就加载它')
    print('如果没存储则提供用记存储后，加载')
    filename='numbers.json'
    try:
        with open(filename,'r') as f:
            username=json.load(f)
    except FileNotFoundError:
        username=input('没有存储，请提用户名：')
        with open(filename,'w') as f:
            json.dump(username,f)
            print(f'欢迎您，{username}')
    else:
        print(f'您好，欢迎回来{username}')
if __name__ =='__main__':
    greet_user()