on_off = True

while on_off:
    guest = input('What is your name?:')
    if guest == 'q':
        on_off = False
    else:
        print(f'{guest.title()} you are wellcome')
        with open('.\\10\guest_book.txt', 'a') as guest_list:
            guest_list.write(f'{guest.title()} are come\n')
