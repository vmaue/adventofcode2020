def calc(line, _min, _max, character):
    for char in line:
        if char == character:
            _max -= (_max-_min)//2+1
        else:
            _min += (_max-_min)//2+1
    return _min

with open('day05/example.txt', 'r') as f:
    print(max([calc(line[:-4], 0, 127, 'F') * 8 + calc(line[-4:-1], 0, 7, 'L') for line in f]))
