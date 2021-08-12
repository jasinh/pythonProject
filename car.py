class Car:
    ''''模拟别的车 '''
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        '''返回整洁描述'''
        long_name=f'{self.make} {self.model} {self.year}'
        return long_name.title()
    def get_odometer(self):
        print(f'this car has {self.odometer_reading} miles on it')
    def update_odometer(self,mile):
        if mile>=self.odometer_reading:
            self.odometer_reading=mile
        else:
            print('u cant roll back an  odo meter')
    def increment_odometer(self,mile):
        if mile<0:
            print('u cant increas fushu')
        else:
            self.odometer_reading+=mile
if __name__=='__main__':
    my_new_car=Car('audi','a4',2019)
    print(my_new_car.get_descriptive_name())
    # my_new_car.get_odometer()
    my_new_car.odometer_reading=23
    my_new_car.get_odometer()
    my_new_car.update_odometer(225)
    my_new_car.increment_odometer(10.23)
    my_new_car.get_odometer()