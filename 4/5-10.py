current_users = ['Lora', 'Vova', 'roma', 'VLAD', 'alex']
new_users = ['vova', 'kiril', 'vlad' , 'Inna', 'dibil']
cc = []
for i in current_users:
    cc.append(i.lower())

for user in new_users:
    if user in cc:
        print(f'{user} exist')
    else:
        print(f'{user} you are wellcome')