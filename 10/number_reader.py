import json

filename = '.\\10\\number.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)