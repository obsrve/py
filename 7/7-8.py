sandwich_orders = ['cheeze_sandwich', 'meat_sandwich', 'fish_sandwich']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f'I made your {current_sandwich.title()}')
    finished_sandwich.append(current_sandwich)

print(finished_sandwich)
