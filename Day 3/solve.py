import os

# Python, why must you torture me?
path = os.path.dirname(os.path.abspath(__file__))
print(f'Running @ {path}')

data = [list(line.rstrip('\n')) for line in open(f'{path}/input.txt', 'r')]

def treecount (data, dx, dy) :
    height = len(data)
    width = len(data[0])
    
    posx = 0
    posy = 0
    
    c = 0
    while posy < height:
        if data[posy][posx] == '#':
            c = c + 1
        posx = (posx + dx) % width
        posy = posy + dy
    return c

t11 = treecount(data, 1, 1)
print(f'({1, 1}): {t11}')
t31 = treecount(data, 3, 1)
print(f'({3, 1}): {t31}')
t51 = treecount(data, 5, 1)
print(f'({5, 1}): {t51}')
t71 = treecount(data, 7, 1)
print(f'({7, 1}): {t71}')
t12 = treecount(data, 1, 2)
print(f'({1, 2}): {t12}')

print(f'Total trees: {t11} {t31} {t51} {t71} {t12}')
print(f'Total "score": {t11*t31*t51*t71*t12}')
