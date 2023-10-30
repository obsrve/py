ingridients = []

while True:
    user_type = input('Chose new ingridients: ')
    if user_type == 'quit':
        break
    else:
        ingridients.append(user_type)
        print(f'{user_type} added')