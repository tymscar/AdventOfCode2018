bags = {}
memo = {}

def how_many_bags_in(bag):

    if bag in memo:
        return memo[bag]

    num_of_bags = 0

    for cont in bags[bag]:
        num_of_bags += cont[1] + cont[1] * how_many_bags_in(cont[0])


    memo[bag] = num_of_bags
    return num_of_bags


def part_2():
    file = open('input.txt', 'r')

    for line in file:
        instruction = line.strip("\n").split(sep=" bags contain ")
        bag = instruction[0]
        contains = []
        containments = instruction[1].split(sep=", ")
        for contain in containments:
            contain_instr = contain.split(sep=" bag")[0]
            how_many = contain_instr[0]
            what = contain_instr[2:]
            if how_many != "n":
                contains.append((what, int(how_many)))
        bags[bag] = contains

    return how_many_bags_in("shiny gold")


print(part_2())
