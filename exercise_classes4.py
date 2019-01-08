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

