def part_1():
    file = open('input.txt', 'r')

    bags = {}

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
                contains.append((what,int(how_many)))
        bags[bag] = contains

    valid_bags = ["shiny gold"]
    run_again = True

    while run_again:
        run_again = False
        for bag in bags:
            for cont in bags[bag]:
                if cont[0] in valid_bags and bag not in valid_bags:
                    valid_bags.append(bag)
                    run_again = True
                    break

    return len(valid_bags) - 1


print(part_1())