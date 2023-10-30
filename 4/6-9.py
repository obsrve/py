favorite_places = {
    'vova' : {
        '1st' : 'home',
        '2nd' : 'forest',
        '3rd' : 'sea',
    },

    'vlad' : {
        '1st' : 'home',
        '2nd' : 'bed',
        '3rd' : 'alco',
    },

    'roma' : {
        '1st' : 'hsfsg',
        '2nd' : 'dfsfaaat',
        '3rd' : 'dfdf'
    },
}

for name, fp in favorite_places.items():
    fv = []
    for i in fp.values():
        fv.append(i)
    print(f'Name: {name.title()}')
    print(f'\tFavorite palce: {fv}')