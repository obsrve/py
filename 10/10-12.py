import json

#user_number = input('What is your favorite number?' )
filename = '.\\10\\fav_numb.json'

def user_number():
    try:
        with open(filename) as f:
            numb = json.load(f)
    except:
        print('Please enter number!')
        user_number = input('What is your favorite number?' )
        with open(filename, 'w') as f:
            numb = json.dump(user_number, f)
    else:
        print(f'Your favorite number is:  {numb}')

user_number()