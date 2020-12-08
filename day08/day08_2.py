with open('day08/example.txt', 'r') as f:
    lst = [line[:-1] for line in f]

instr_to_find = ('jmp', 'nop')
indices = [i for i, x in enumerate(lst) if x[:3] in instr_to_find]

for idx in indices:
    accumulator = 0
    i = 0
    instr_lst = []

    while i not in instr_lst and i < len(lst):
        instr_lst.append(i)
        instr, nb = lst[i].split(' ')
        nb = int(nb)
        if i == idx:
            instr = 'nop' if instr == 'jmp' else 'jmp'
        if instr == 'jmp':
            i += nb
            continue
        if instr == 'acc':
            accumulator += nb
        i += 1
    if i not in instr_lst:
        print(f"accumulator: {accumulator}")
        break
