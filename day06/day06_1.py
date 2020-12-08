with open('day06/example.txt', 'r') as f:
    print(sum(len(set(group.replace('\n', ''))) for group in f.read()[:-1].split('\n\n')))
