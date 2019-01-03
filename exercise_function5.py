#8-12
# def sandwich_items(*food):
#     print(food)

# sandwich_items('chicken', 'lettuce', 'tomato')
# sandwich_items('mayo')
# sandwich_items('ketchup', 'cheese')

#8-13
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user. """
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile('samantha', 'chia', location='singapore',age='20',birthday='11/11/1999')
# print(user_profile)

#8-14
def store_car_info(manufaturer,model_name,**car_info):
    car = {}
    car['manufaturer'] = manufaturer
    car['model_name'] = model_name
    for key,value in car_info.items():
        car[key] = value
    return car

certain_car_info = store_car_info('subaru', 'outback', color='blue', tow_package=True)
print(certain_car_info)
