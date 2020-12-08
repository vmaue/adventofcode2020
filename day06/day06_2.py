with open('day06/example.txt', 'r') as f:
    groups = f.read()[:-1].split('\n\n')

lst = []
for group in groups:
    peoples = group.split('\n')
    unique_votes = set(group.replace('\n', ''))
    vote_count = {}
    for people in peoples:
        for vote in people:
            vote_count[vote] = vote_count[vote] + 1 if vote in vote_count else 1
    lst.append(sum(val == len(peoples) for val in vote_count.values()))

print(sum(lst))
