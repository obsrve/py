cities = {
    'kyiv' : {
        'country' : "kyiv",
        'population' : '43m',
    },
    'pidarasha' : {
        'country' : 'pidary',
        'population' : '153m',
    },
}

for name, county in cities.items():
    print(f'{name}')
    for k,v in county.items():
        print(f"\t{k} : {v}")