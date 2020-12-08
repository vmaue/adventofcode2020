with open('day04/example.txt', 'r') as f:
    lst = f.read()[:-1].split('\n\n')

def check_btwn(_str, _min, _max):
    try:
        val = int(_str)
    except:
        return False
    return _min <= val <= _max

def check_hgt(hgt):
    unit = hgt[-2:]
    try:
        val = int(hgt[:-2])
    except:
        return False
    return (150 <= val <= 193) if unit == 'cm' else (59 <= val <= 76)

def check_hcl(hcl):
    _str = '0123456789abcdef'
    return len(hcl) == 7 and hcl[0] == '#' and all([char in hcl for char in hcl])

def check_ecl(ecl):
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in eye_colors

def check_pid(pid):
    try:
        val = int(pid)
    except:
        return False
    return len(pid) == 9

passport_fields = {
    'byr': lambda byr: check_btwn(byr, 1920, 2002),
    'iyr': lambda iyr: check_btwn(iyr, 2010, 2020),
    'eyr': lambda eyr: check_btwn(eyr, 2020, 2030),
    'hgt': check_hgt,
    'hcl': check_hcl,
    'ecl': check_ecl,
    'pid': check_pid
}

res = []
for passport in lst:
    dct = {}
    for passport_field in passport.replace('\n', ' ').split(' '):
        key, val = passport_field.split(':')
        dct[key] = val
    res.append(all([func(dct[passport_field]) if passport_field in dct else False for passport_field, func in passport_fields.items()]))

print(sum(res))
