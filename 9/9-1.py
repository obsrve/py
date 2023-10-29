class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f'Restaurant name - {self.name}')
        print(f'Cuisine typ is - {self.type}')
    
    def open_restaurant(self):
        print(f'{self.name} is open!')
    
res1 = Restaurant('Gaga', 'Georigain')

print(f'{res1.name}')
print(f'{res1.type}')

res1.describe_restaurant()
res1.open_restaurant()
