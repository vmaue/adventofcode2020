from functools import reduce

with open('day03/example.txt', 'r') as f:
    lst = [line[:-1] for line in f]

trees = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for slope in slopes:
    i = 0
    nb_tree = 0
    for line in lst[::slope[1]]:
        nb_tree += 1 if line[i] == '#' else 0
        i = (i + slope[0]) % len(line)
    trees.append(nb_tree)

print(reduce(lambda x, y: x*y, trees))
