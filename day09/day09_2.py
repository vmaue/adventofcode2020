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

i = sum_of_prev(25)

def find_contiguous_sum(i):
    for a in range(i+1):
        b = a+1
        _range = (a, b)
        _sum = 0
        while _sum < lst[i]:
            b += 1
            _range = (a, b)
            tmp = [lst[w] for w in range(a, _range[1])]
            _sum = sum(tmp)
            if _sum == lst[i]:
                print(sum((max(tmp), min(tmp))))
                return

find_contiguous_sum(i)
