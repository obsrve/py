import json

user_number = input('What is your favorite number?' )
filename = '.\\10\\fav_numb.json'

with open(filename, 'w') as f:
    numb = json.dump(user_number, f)

with open(filename) as f:
    numb = json.load(f)
    print(f'Your favorite number is:  {numb}')