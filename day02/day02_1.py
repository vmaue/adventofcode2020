with open('day02/example.txt', 'r') as f:
    lst = [line for line in f]

def is_ok(line):
    minmax, char, password = line.split(' ')
    _min, _max = (int(nb) for nb in minmax.split('-'))
    return _min <= password.count(char[0]) <= _max

print(sum(is_ok(line) for line in lst))
