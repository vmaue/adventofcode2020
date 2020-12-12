with open('day11/example.txt', 'r') as f:
    lst = [line[:-1] for line in f]

def lst_to_str(lst):
    return '\n'.join(lst)

def is_occupied(i, j, lst):
    tmp = [-1, 0, 1]
    nb_occupied = 0
    for a in tmp:
        for b in tmp:
            x, y = a+i, b+j
            if (a == 0 and b == 0) or x < 0 or y < 0 or x >= len(lst) or y >= len(lst[0]):
                continue
            if lst[x][y] == '#':
                nb_occupied += 1
    return nb_occupied

def create_list(lst):
    final = []
    for i in range(len(lst)):
        line = []
        for j in range(len(lst[i])):
            char = '.'
            if lst[i][j] == '.':
                line.append('.')
                continue
            elif lst[i][j] == 'L':
                if is_occupied(i, j, lst) == 0:
                    line.append('#')
                else:
                    line.append('L')
            else:
                if is_occupied(i, j, lst) >= 4:
                    line.append('L')
                else:
                    line.append('#')
        final.append(''.join(line))
    return final

while True:
    before = lst_to_str(lst)
    lst = create_list(lst)
    after = lst_to_str(lst)
    if before == after:
        print(before.count('#'))
        break
