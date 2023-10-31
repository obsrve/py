from random import choice

win_tick = []
def random():
    numb = [4, 2, 8, 5, 1, 9, 0, 3, 6, 7, 'b', 't', 'e', 'i']
    i = 0
    while i < 4:
        a = choice(numb)
        win_tick.append(a)
        i += 1
  
random()
print(f'That ticket are winner : {win_tick}')