class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 6
    
    def describe_restaurant(self):
        print(f'Restaurant name - {self.name}')
        print(f'Cuisine typ is - {self.type}')
    
    def open_restaurant(self):
        print(f'{self.name} is open!')

    def set_number_served(self, clients):
        self.number_served = clients
    
    def increment_number_served(self, addit_clients):
        self.number_served += addit_clients
    
    
res1 = Restaurant('Gaga', 'Georigain')
#res1.set_number_served(10)
res1.increment_number_served(349)

print(f'{res1.name}')
print(f'{res1.type}')
print(f'Numbers of clients: {res1.number_served}\n')

res1.describe_restaurant()
res1.open_restaurant()



