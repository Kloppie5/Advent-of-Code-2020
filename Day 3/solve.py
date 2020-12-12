import os

# Python, why must you torture me?
path = os.path.dirname(os.path.abspath(__file__))
print(f'Running @ {path}')

data = [list(line.rstrip('\n')) for line in open(f'{path}/input.txt', 'r')]

height = len(data)
width = len(data[0])

right = 3
down = 1

posx = 0
posy = 0

c = 0
while posy < height:
    print(f'({posx}, {posy}): {data[posy][posx]}')
    if data[posy][posx] == '#':
        c = c + 1
    posx = (posx + right) % width
    posy = posy + down
print(c)
