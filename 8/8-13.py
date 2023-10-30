def build_profile(first, last, **user_info):
    #create user_info list
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Vladimir', 'Shkvarun', location='Vyshneve', age='29', )
print(user_profile)