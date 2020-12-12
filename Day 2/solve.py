import os

# Python, why must you torture me?
path = os.path.dirname(os.path.abspath(__file__))
print(f'Running @ {path}')

c = 0
for line in open(f'{path}/input.txt', 'r'):
    data = line.rstrip('\n').split(' ')
    data = {'min': int(data[0].split('-')[0]), 'max': int(data[0].split('-')[1]), 'letter': data[1].split(':')[0], 'password': data[2]}
    occ = data['password'].count(data['letter'])
    if data['min'] <= occ and occ <= data['max']:
        # print(f"{data} is valid")
        c = c + 1
print(c)
