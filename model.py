from random import randint
class Die:
    def __init__(self,times,sides=6):
        self.times=times
        self.sides=sides
    def roll_die(self):
        for time in range(self.times):
            print(f'第{time+1}次',randint(1,self.sides))
if __name__ == '__main__':
    six=Die(100)
    six.roll_die()
    print('-----分割---')
    ten=Die(100,10)
    ten.roll_die()
    print('------分割------')
    twen=Die(100,20)
    twen.roll_die()