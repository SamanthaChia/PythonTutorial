#8-12
# def sandwich_items(*food):
#     print(food)

# sandwich_items('chicken', 'lettuce', 'tomato')
# sandwich_items('mayo')
# sandwich_items('ketchup', 'cheese')

#8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user. """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('samantha', 'chia', location='singapore',age='20',birthday='11/11/1999')
print(user_profile)