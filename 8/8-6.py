def city_country(city, country):
    location = (f'"{city}, {country}"')
    return location.title()

pairs = city_country('kyiv', 'Ukraine')
print(pairs)
pairs = city_country('eul', 'korea')
print(pairs)
pairs = city_country('warshava', 'polska')
print(pairs)