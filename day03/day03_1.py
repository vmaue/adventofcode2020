with open('day03/example.txt', 'r') as f:
    lst = [line[:-1] for line in f]

slope = (3, 1)
i = 0
nb_tree = 0
for line in lst:
    nb_tree += 1 if line[i] == '#' else 0
    i = (i + slope[0]) % len(line)

print(nb_tree)
