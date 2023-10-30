class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f'Restaurant name - {self.name}')
        print(f'Cuisine typ is - {self.type}\n')
    
    def open_restaurant(self):
        print(f'{self.name} is open!')
    
res1 = Restaurant('Gaga', 'Georigain')
res2 = Restaurant('Home', 'Ukrainian')
res3 = Restaurant('Kavichi', 'Japan')

res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()

