friend_vlad = {
    'first_name' : 'Vlad',
    'last_name' : 'Vdovitsa',
    'age' : '28',
    'city' : 'Vyshneve',
    'lang' : 'Vue',
    'family' : 'yes',
    }

friend_vova = {
    'first_name' : 'Vova',
    'last_name' : 'shkvarun',
    'age' : '29',
    'city' : 'Vyshneve',
    'lang' : 'python',
    'family' : 'no',
    }

friend_roma = {
    'first_name' : 'roma',
    'last_name' : 'litvin',
    'age' : '32',
    'city' : 'troya',
    'lang' : 'cmd',
    'family' : 'yes',
    }

people = [friend_vlad, friend_vova, friend_roma]
for name in people:
    print(name)
    for k,v in name.items():
        print(f'{k} : {v}\n')
