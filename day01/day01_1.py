import itertools

with open('day01/example.txt', 'r') as f:
    lst = [int(line) for line in f]

for possibility in itertools.combinations(lst, 2):
    if sum(possibility) == 2020:
        print(possibility[0]*possibility[1])
        break
