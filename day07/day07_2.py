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
            bags.append({"bag_name": f"{tmp[1]} {tmp[2]}", "bag_nb": int(tmp[0])})
    bag_dct[bag] = bags

def nb_bags(key):
    total = 1
    for bag in bag_dct[key]:
        total += bag['bag_nb'] * nb_bags(bag['bag_name'])
    return total

print(nb_bags('shiny gold')-1)
