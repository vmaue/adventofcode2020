with open('day11/example.txt', 'r') as f:
    lst = [line[:-1] for line in f]

def lst_to_str(lst):
    return '\n'.join(lst)

def is_occupied(i, j, lst):
    nb_occupied = 0
    for a in range(i-1, -1, -1):
        if lst[a][j] == '#':
            nb_occupied += 1
            break
        if lst[a][j] == 'L':
            break
    for a in range(i+1, len(lst)):
        if lst[a][j] == '#':
            nb_occupied += 1
            break
        if lst[a][j] == 'L':
            break
    for b in range(j-1, -1, -1):
        if lst[i][b] == '#':
            nb_occupied += 1
            break
        if lst[i][b] == 'L':
            break
    for b in range(j+1, len(lst[i])):
        if lst[i][b] == '#':
            nb_occupied += 1
            break
        if lst[i][b] == 'L':
            break
    for a, b in zip(range(i-1, -1, -1), range(j-1, -1, -1)):
        if lst[a][b] == '#':
            nb_occupied += 1
            break
        if lst[a][b] == 'L':
            break
    for a, b in zip(range(i+1, len(lst)), range(j+1, len(lst[i]))):
        if lst[a][b] == '#':
            nb_occupied += 1
            break
        if lst[a][b] == 'L':
            break
    for a, b in zip(range(i-1, -1, -1), range(j+1, len(lst[i]))):
        if lst[a][b] == '#':
            nb_occupied += 1
            break
        if lst[a][b] == 'L':
            break
    for a, b in zip(range(i+1, len(lst)), range(j-1, -1, -1)):
        if lst[a][b] == '#':
            nb_occupied += 1
            break
        if lst[a][b] == 'L':
            break
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
                if is_occupied(i, j, lst) >= 5:
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
