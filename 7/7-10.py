respons = {}

req_active = True

while req_active:
    name = input('\nEnter you name:')
    respon = input('Where do you want to go?')
    respons[name] = respon

    repeat = input('Would you like to repeat? (yes / no)')
    if repeat == 'no':
        req_active = False

print('---Results---')
for name, respon in respons.items():
    print(f'{name} want to go to {respon}')