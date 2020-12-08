with open('day08/example.txt', 'r') as f:
    lst = [line[:-1] for line in f]

accumulator = 0
i = 0
instr_lst = []

while i not in instr_lst:
    instr_lst.append(i)
    instr, nb = lst[i].split(' ')
    nb = int(nb)
    if instr == 'jmp':
        i += nb
        continue
    if instr == 'acc':
        accumulator += nb
    i += 1

print(accumulator)
