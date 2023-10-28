active = True
while active:
    age = input('Enter youre age: ')
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age <= 3:
            print('you are free to  pay')
        elif age > 3 and age <= 12:
            print('you must pay 10$')
        elif age > 12:
            print('you must pay 15$')
        