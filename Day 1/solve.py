import os

# Python, why must you torture me?
path = os.path.dirname(os.path.abspath(__file__))
print(f'Running @ {path}')

wo = [int(line.rstrip('\n')) for line in open(f'{path}/input.txt', 'r')]
wo.sort()

target = 2020
print(f'Finding the product of the two numbers that sum to {target}')
for el in wo:
    if (2020-el in wo):
        print(f'Found {el}; {el*(2020-el)}')

print(f'Finding the product of the three numbers that sum to {target}')
n = len(wo)
for k in range(0, n):
    for j in range(k, n):
        if target - wo[k] - wo[j] in wo:
            print(f'Found {target-wo[k]-wo[j]} {wo[j]} {wo[k]} : {(target-wo[k]-wo[j])*wo[j]*wo[k]}')
