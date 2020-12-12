with open('day12/example.txt', 'r') as f:
    lst = [line[:-1] for line in f]

x, y = 0, 0
facing = 'E'
directions = 'NESW'

for instr in lst:
    direction, val = instr[0], int(instr[1:])
    if direction == 'F':
        if facing == 'E' or facing == 'W':
            x += val if facing == 'E' else -val
        else:
            y += val if facing == 'N' else -val
    elif direction == 'N':
        y += val
    elif direction == 'S':
        y -= val
    elif direction == 'E':
        x += val
    elif direction == 'W':
        x -= val
    elif direction == 'R':
        facing = directions[(directions.index(facing) + val // 90)%len(directions)]
    elif direction == 'L':
        facing = directions[(4 + directions.index(facing) - val // 90)%len(directions)]

print(abs(x)+abs(y))
