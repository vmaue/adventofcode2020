with open('day02/example.txt', 'r') as f:
    lst = [line for line in f]

def is_ok(line):
    minmax, char, password = line.split(' ')
    _min, _max = (int(nb) for nb in minmax.split('-'))
    char = char[0]
    return sum((password[_min-1]==char, password[_max-1]==char)) == 1

print(sum(is_ok(line) for line in lst))
