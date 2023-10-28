user_list = []
if user_list:
    for user in user_list:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for loggin in again')
else:
    print('We need to find some users!')