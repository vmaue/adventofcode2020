with open('day07/example.txt', 'r') as f:
    lst = [line[:-1] for line in f]

bag_dct = {}
for line in lst:
    bag, rest = line.split(' bags contain ')
    splited = rest.split(', ')
    bags = []
    if splited[0] != "no other bags.":
        for bg in splited:
            tmp = bg.split(' ')
            bags.append(f"{tmp[1]} {tmp[2]}")
    bag_dct[bag] = bags

tmp_bag_dct = bag_dct.copy()

possible_bags = []

for key, val in bag_dct.items():
    if 'shiny gold' in val:
        possible_bags.append(key)
        del tmp_bag_dct[key]

for i in range(5):
    for key, val in bag_dct.items():
        for elem in possible_bags:
            if elem in val:
                possible_bags.append(key)
                tmp_bag_dct.pop(key, None)

print(len(set(possible_bags)))
