while True:
    num1 = input('first numb:')
    num2 = input('second numb:')

    try:
        sum = int(num1) + int(num2)
    except:
        print('Incorrect value')
    else:
        print(sum)