import itertools

with open('day09/example.txt', 'r') as f:
    lst = [int(line[:-1]) for line in f]

def sum_of_prev(preamble):
    for i in range(preamble, len(lst)-1):
        for possibility in itertools.combinations(lst[i-preamble:i], 2):
            if sum(possibility) == lst[i]:
                break
        else:
            return i

print(lst[sum_of_prev(25)])
