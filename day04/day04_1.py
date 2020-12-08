with open('day04/example.txt', 'r') as f:
    lst = f.read()[:-1].split('\n\n')

passport_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

res = []
for passport in lst:
    dct = {}
    for passport_field in passport.replace('\n', ' ').split(' '):
        key, val = passport_field.split(':')
        dct[key] = val
    res.append(all([True if passport_field in dct else False for passport_field in passport_fields]))

print(sum(res))
