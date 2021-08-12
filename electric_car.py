class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0
        self.gas=0

    def get_descriptive_name(self):
        long_name=f'{self.make} {self.model} {self.year}'
        return long_name.title()

    def read_odometer(self):
        print(f'this car has {self.odometer} miles on it.')

    def update_odometer(self,mile):
        if mile>=self.odometer:
            self.odometer=mile
        else:
            print('u cant roll back odo meter')

    def increment_odometer(self,mile):
        if mile>0:
            self.odometer+=mile
        else:
            print('u cant increment negtive number')

    def fill_gas_tank(self,gas):
        if gas >0:
            self.gas=+gas
        else:
            print(f'can fill negtive gas')


class Battery:
    def __init__(self,battery_size=75):
        self.battery_size=battery_size

    def describe_battery(self):
        print(f'this cas has {self.battery_size}-kwH battery')

    def get_range(self):
        if self.battery_size==75:
            range=260
        else:
            range=315
        print(f'this car can go about {range} miles away on fullcharge')

    def upgrade_battery(self):
        if self.battery_size!=100:
            self.battery_size=100


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
    def fill_gas_tank(self,gas=None):
        if gas:
            print(f'{gas},but no need to fill oil')
        else:
            print(f'no need to fill oil')


if __name__=='__main__':
    mytesla=ElectricCar('telsa','models',2019)
    print(mytesla.get_descriptive_name())
    mytesla.battery.describe_battery()
    mytesla.fill_gas_tank(33)
    ptcar=Car('ge','orlando',2019)
    ptcar.fill_gas_tank(299)
    print(ptcar.gas)
    mytesla.battery.get_range()
    mytesla.battery.upgrade_battery()
    mytesla.battery.get_range()
