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

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print("First Name : " + self.first_name)
        print("Last Name : " + self.last_name)
        print("Age : " + str(self.age))
    
    def greet_user(self):
        print("Hello , " + self.first_name + " " + self.last_name)
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)

admin1 = Admin('sam', 'chia', '50')
admin1.show_privileges()