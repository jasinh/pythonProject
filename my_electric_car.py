from electric_car import Car as C,ElectricCar as Ec
# from car import *
mytesla=Ec('tesla','models',2019)
print(mytesla.get_descriptive_name())
mytesla.battery.describe_battery()
mytesla.battery.get_range()
my_oil_car=C('byd','tang',2020)
print(my_oil_car.get_descriptive_name())
my_oil_car.read_odometer()
my_oil_car.fill_gas_tank(1000)
print(my_oil_car.gas,type(mytesla))

