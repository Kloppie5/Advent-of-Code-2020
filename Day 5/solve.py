import os

# Python, why must you torture me?
path = os.path.dirname(os.path.abspath(__file__))
print(f'Running @ {path}')

ids = []
for line in open(f'{path}/input.txt', 'r').read().split('\n'):
    id = int(line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0'), 2)
    ids.append(id)
ids.sort()

prev = ids[0]
for id in ids:
    if id == prev + 2:
        print(id-1)
    prev = id
