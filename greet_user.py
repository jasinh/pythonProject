import json

filename = 'numbers.json'


def get_stored_username():
    '''如果 存储了就获取 它'''
    try:
        with open(filename,'r') as f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_name():
    username = input("what is your name:")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
def greet_user():
    username=get_stored_username()
    if username:
        print(f"welcome {username}")
    else:
        print(f'we wellcom u come back ,{get_new_name()}')


if __name__ =="__main__":
    greet_user()