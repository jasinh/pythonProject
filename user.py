class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempt=0
    def describe_user(self):
        long_name=f'{self.first_name} {self.last_name}'
        print(long_name.title())
    def greet_user(self):
        print(f'hello, {self.first_name} {self.last_name}')
    def increment_login_attempts(self):
        self.login_attempt+=1
    def reset_login_attempts(self):
        self.login_attempt=0
if __name__ =='__main__':
    user1=User('huang','xing')
    user1.greet_user()
    user1.describe_user()
    user2=User('wang','xin')
    user2.greet_user()
    user2.describe_user()
    user2.increment_login_attempts()
    user2.increment_login_attempts()
    print(user2.login_attempt)
    user2.reset_login_attempts()
    print(user2.login_attempt)