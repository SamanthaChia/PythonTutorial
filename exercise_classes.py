# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
    
#     def describe_restaurant(self):
#         print("The restaurant's name is " + self.restaurant_name)
#         print("The cuisine type is " + self.cuisine_type)
    
#     def open_restaurant(self):
#         print(self.restaurant_name + " is open!")

# restaurant = Restaurant('restaurant name', 'japanese')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant2 = Restaurant('McDonalds','western')
# restaurant2.describe_restaurant()

# restaurant3= Restaurant('Sushi Tei', 'Japanese')
# restaurant3.describe_restaurant()

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def describe_user(self):
        print("First Name : " + self.first_name)
        print("Last Name : " + self.last_name)
        print("Age : " + str(self.age))
    
    def greet_user(self):
        print("Hello , " + self.first_name + " " + self.last_name)

user1 = User('sam', 'chia', 20)
user2 = User('owen', 'lee', 20)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()