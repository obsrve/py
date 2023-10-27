sandwich_orders = ['cheeze_sandwich', 'pastrami_sandwich', 'meat_sandwich', 'pastrami_sandwich', 'fish_sandwich', 'pastrami_sandwich']
print('we have not pastrami')

while 'pastrami_sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami_sandwich')

print(sandwich_orders)