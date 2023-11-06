while True:
    question = input('Why yoy love programming?:')
    with open('.\\10\\answer.txt', 'a') as anw:
        anw.write(f'{question}\n')