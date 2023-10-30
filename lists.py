#START
# [] - it`s list

bicycle = ['trek', 'redline', 'specialized']
print(bicycle[1])
print(bicycle[0].title())
print(bicycle[-1])

#list value in str
message = f"My first bicycle was a {bicycle[1].title()}."
print(message)

#MADE

names = ['Vladimir', 'Alexander', 'Vladislav']
cars = ['bmw', 'audi', 'opel']
print(f"Hello, {names[0]}, your car is {cars[1].title()}")

#################################################
motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)
#add new item in list / .append()
motorcycle.append('ducati')
print(motorcycle)
#insert new item / .insert()
motorcycle.insert(1, 'bmw')
print(motorcycle)

#delete item from list
del motorcycle[1]
print(motorcycle)


#pop() deactivate  item from list(if pop have`t index it take last item from list`)
poped_motorcycle = motorcycle.pop(0)
print(motorcycle)
print(poped_motorcycle)

#remove item , knowing only value
motorcycle.remove('suzuki')
print(motorcycle)