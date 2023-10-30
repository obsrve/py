def describe_city(city_name, country_name='Ukraine'):
    print(f'{city_name.title()} is in {country_name.title()}')

describe_city('Kyiv')
describe_city('London','Great Britan')
describe_city(country_name='USA', city_name='New York')