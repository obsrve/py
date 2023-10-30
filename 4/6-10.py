fav_namb = {
    'vova' : ['17', '1'],
    'vlad' : ['23', '2'],
    'roma' : ['35', '6'],
    'serh' : ['55', '8'],
}

for name, namb in fav_namb.items():
    print(f"{name.title()}, your favorite numbers:")
    for nb in namb:
        print(f"\t{nb}")