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
    

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['white', 'black', 'red']
    
    def show_flavors(self):
        print(f'You flavors: {self.flavors}')


res1 = IceCreamStand('Gaga', 'Georigain')
res1.show_flavors()