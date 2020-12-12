import os

# Python, why must you torture me?
path = os.path.dirname(os.path.abspath(__file__))
print(f'Running @ {path}')

cs = 0
ct = 0
for line in open(f'{path}/input.txt', 'r'):
    data = line.rstrip('\n').split(' ')
    data = {'a': int(data[0].split('-')[0]), 'b': int(data[0].split('-')[1]), 'letter': data[1].split(':')[0], 'password': data[2]}
    occ = data['password'].count(data['letter'])
    if data['a'] <= occ and occ <= data['b']:
        print(f"{data} is valid following the sled requirements")
        cs = cs + 1
    if bool(data['password'][data['a']-1] == data['letter']) ^ bool(data['password'][data['b']-1] == data['letter']):
        print(f"{data} is valid following the toboggan requirements")
        ct = ct + 1
print(f'{cs} valid passwords following the sled requirements')
print(f'{ct} valid passwords following the toboggan requirements')
