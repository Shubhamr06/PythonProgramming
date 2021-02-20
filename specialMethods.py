# Python Special Methods
# In this program , we are going to find the lenth of class variable , Also we can delete objects created in a class


class Mobile():

    def __init__(self,brand,battery,country):
        self.brand = brand
        self.battery = battery
        self.country = country

    def __len__(self):
        return self.battery

    def __str__(self):
        return f"{self.brand} by {self.country}"

my_mobile = Mobile('asus' , 5000 , 'korean')
print(len(my_mobile.brand))
print(my_mobile.country)
print(len(my_mobile.country))
print(str(my_mobile))
print(len(my_mobile))


