import os

# Python, why must you torture me?
path = os.path.dirname(os.path.abspath(__file__))
print(f'Running @ {path}')

wo = [int(line.rstrip('\n')) for line in open(f'{path}/input.txt', 'r')]
wo.sort()


target = 2020
for el in wo:
    if (2020-el in wo):
        print(f'Found {el}; {el*(2020-el)}')
