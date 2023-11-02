import json

username = input('Enter your name:')

filename = '.\\10\\username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"we`ll remember you when you come back, {username}")
    