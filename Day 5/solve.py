import os

# Python, why must you torture me?
path = os.path.dirname(os.path.abspath(__file__))
print(f'Running @ {path}')

max = 0
for line in open(f'{path}/input.txt', 'r').read().split('\n'):
    id = int(line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0'), 2)
    if id > max:
        max = id
print(max)

