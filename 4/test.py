rivers = {
    'nile' : 'egept',
    'dnipro' : 'kyiv',
    'homora' : 'polonne',
}

for river, country in rivers.items():
    print(f'{river.title()} is in {country.title()}')

for river in rivers.keys():
    print(f"{river}")

for country in rivers.values():
    print(country)


fav_lang = {
    'sarah' : 'c',
    'edward' : 'ruby',
    'vlad' : 'js',
    'vova' : 'python',
}
