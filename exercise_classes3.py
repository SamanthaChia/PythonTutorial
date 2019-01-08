# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
    
#     def describe_restaurant(self):
#         print("The restaurant's name is " + self.restaurant_name)
#         print("The cuisine type is " + self.cuisine_type)
    
#     def open_restaurant(self):
#         print(self.restaurant_name + " is open!")
    
#     def set_number_served(self,new_value):
#         self.number_served = new_value
    
#     def increment_number_served(self, increment_value):
#         self.number_served = self.number_served + increment_value

# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ['chocolate', 'strawberry', 'vanilla', 'mint']
    
#     def display_flavors(self):
#         print("The available flavors are : " + str(self.flavors))

# ice_cream_stand = IceCreamStand('Ben&Jerry', 'western')
# ice_cream_stand.display_flavors()

# class User():
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = 0
    
#     def describe_user(self):
#         print("First Name : " + self.first_name)
#         print("Last Name : " + self.last_name)
#         print("Age : " + str(self.age))
    
#     def greet_user(self):
#         print("Hello , " + self.first_name + " " + self.last_name)
    
#     def increment_login_attempts(self):
#         self.login_attempts += 1
    
#     def reset_login_attempts(self):
#         self.login_attempts = 0

# class Privileges():
#     def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
#         self.privileges = privileges

#     def show_privileges(self):
#         print(self.privileges)

# class Admin(User):
#     def __init__(self, first_name, last_name, age):
#         super().__init__(first_name, last_name, age)
#         self.privileges = Privileges()


# admin1 = Admin('sam', 'chia', '50')
# admin1.privileges.show_privileges()

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage. """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """ 
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading. """
        self.odometer_reading += miles
        
class Battery():
    """A simple attempt to model a battery for an electric car. """
    
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if(self.battery_size != 85):
            self.battery_size = 85
        

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """

        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()