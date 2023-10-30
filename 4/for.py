pizzas = ['Carbonara', 'Paperoni', '4 Cheeze']
for pizza in pizzas:
    print(f"I like {pizza} pizza!")
print("I really love pizza!.\n")

animals = ['dog', 'cat', 'elephant']
for animal in animals:
    print(animal)


friend_pizzas = pizzas[:]
pizzas.append('Gavaya')
friend_pizzas.append('Beef')


print(pizzas)
print(friend_pizzas)