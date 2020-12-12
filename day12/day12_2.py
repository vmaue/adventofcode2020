with open('day12/example.txt', 'r') as f:
    lst = [line[:-1] for line in f]

x, y = 0, 0
waypoint = (10, 1)

for instr in lst:
    direction, val = instr[0], int(instr[1:])
    if direction == 'F':
        x += val*waypoint[0]
        y += val*waypoint[1]
    elif direction == 'N':
        waypoint = (waypoint[0], waypoint[1]+val)
    elif direction == 'S':
        waypoint = (waypoint[0], waypoint[1]-val)
    elif direction == 'E':
        waypoint = (waypoint[0]+val, waypoint[1])
    elif direction == 'W':
        waypoint = (waypoint[0]-val, waypoint[1])
    else:
        val = val // 90
        if direction == 'L':
            val = 1 if val == 3 else 3 if val == 1 else val
        if val == 1:
            waypoint = (waypoint[1], -waypoint[0])
        elif val == 2:
            waypoint = (-waypoint[0], -waypoint[1])
        elif val == 3:
            waypoint = (-waypoint[1], waypoint[0])

print(abs(x)+abs(y))
