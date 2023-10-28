guests = ['Albert', 'Tesla', 'Jack', 'Da Vinchi']
#guests[-1] = 'Abbadon'
#print(guests)
guests.insert(0, 'Vova') 
guests.insert(3, 'Sasha')
guests.append('Me')
print("I am sorry, my  dinner table will not delivery intime")

popguest = guests.pop()
print(f"{popguest},i am sorry")
popguest = guests.pop()
print(f"{popguest},i am sorry")
popguest = guests.pop()
print(f"{popguest},i am sorry")
popguest = guests.pop()
print(f"{popguest},i am sorry")
popguest = guests.pop()
print(f"{popguest},i am sorry")
for i in guests:
    print(f"{i}, you are wellcome")

del guests[0]
del guests[0]
print(guests)

#for i in guests:
#   print(f"{i},i found bigger dinner table?")