user_name = input('Enter your name:')

with open('.\\10\\users.txt', 'a') as file:
    file.write(f'{user_name}\n')