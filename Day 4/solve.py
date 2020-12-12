import os

# Python, why must you torture me?
path = os.path.dirname(os.path.abspath(__file__))
print(f'Running @ {path}')

c = 0
for line in open(f'{path}/input.txt', 'r').read().split('\n\n'):
    passport = {}
    for kvp in line.replace('\n', ' ').split(' '):
        k = kvp.split(':')[0]
        v = kvp.split(':')[1]
        passport[k] = v
    valid = True
    for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if not k in passport:
            print(f'Passport missing key \'{k}\'')
            valid = False
    if valid:
        print(f'{passport} is valid')
        c = c + 1
print(c)
