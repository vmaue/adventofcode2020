with open('day10/example.txt', 'r') as f:
    lst = [int(line[:-1]) for line in f]

lst.append(0)
lst = sorted(lst)

nbs = {}
def fn(idx):
    if idx+1 == len(lst):
        return 1
    elif idx in nbs:
        return nbs[idx]
    nb = 0
    nxt = idx + 1
    while nxt < len(lst) and lst[nxt] - lst[idx] <= 3:
        nb += fn(nxt)
        nxt += 1
    nbs[idx] = nb
    return nb

print(fn(0))
