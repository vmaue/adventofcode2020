with open('day10/example.txt', 'r') as f:
    lst = [int(line[:-1]) for line in f]

def find_adapter(lst, i, a, b, c):
    lst = lst.copy()
    if i+1 in lst:
        lst.remove(i+1)
        find_adapter(lst, i+1, a+1, b, c)
    elif i+2 in lst:
        lst.remove(i+2)
        find_adapter(lst, i+2, a, b+1, c)
    elif i+3 in lst:
        lst.remove(i+3)
        find_adapter(lst, i+3, a, b, c+1)
    else:
        print((a)*(c+1))

find_adapter(lst, 0, 0, 0, 0)
