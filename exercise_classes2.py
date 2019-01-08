class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name)
        print("The cuisine type is " + self.cuisine_type)
    
    def open_restaurant(self):
        print(self.restaurant_name + " is open!")
    
    def set_number_served(self,new_value):
        self.number_served = new_value
    
    def increment_number_served(self, increment_value):
        self.number_served = self.number_served + increment_value

restaurant = Restaurant('restaurant name', 'japanese')
restaurant.set_number_served(20)
restaurant.increment_number_served(10)
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.number_served)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant2 = Restaurant('McDonalds','western')
# restaurant2.describe_restaurant()

# restaurant3= Restaurant('Sushi Tei', 'Japanese')
# restaurant3.describe_restaurant()