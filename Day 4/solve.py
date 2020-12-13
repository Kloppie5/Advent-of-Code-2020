import os
import string

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
            break
    if not valid:
        continue

    byr = int(passport['byr'])
    if byr < 1920 or byr > 2002:
        print(f'byr {byr} out of range')
        continue
    
    iyr = int(passport['iyr'])
    if iyr < 2010 or iyr > 2020:
        print(f'iyr {iyr} out of range')
        continue
    
    eyr = int(passport['eyr'])
    if eyr < 2020 or eyr > 2030:
        print(f'eyr {eyr} out of range')
        continue
    
    hgttype = passport['hgt'][-2:]
    hgt = int(passport['hgt'][0:-2])
    if hgttype == 'cm' and (hgt < 150 or hgt > 193) or hgttype == 'in' and (hgt < 59 or hgt > 76) or not hgttype in ['cm', 'in']:
        print(f'hgt {hgt} {hgttype} out of range')
        continue

    hcl = passport['hcl']
    if len(hcl) != 7 or hcl[0] != '#' or not all(c in string.hexdigits for c in hcl[1:]):
        print(f'hcl {hcl} has invalid format')
        continue

    ecl = passport['ecl']
    if not ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: 
        print(f'ecl {ecl} has invalid format')
        continue

    pid = passport['pid']
    if len(pid) != 9 or not all(c in string.digits for c in pid):
        print(f'pid {pid} has invalid format')
        continue
    
    print(f'{passport} is valid')
    c = c + 1

print(f'{c} passports are valid')
