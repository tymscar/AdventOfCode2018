def part_1():
    file = open('input.txt', 'r')
    memory = {}

    for line in file:
        line = line.strip("\n").split(" = ")
        if line[0] == "mask":
            ormask = 36 * ["0"]
            andmask = 36 * ["1"]
            for i, char in enumerate(line[1]):
                if char == "1":
                    ormask[i] = "1"
                if char == "0":
                    andmask[i] = "0"
            ormask = int("".join(ormask), 2)
            andmask = int("".join(andmask), 2)
        else:
            location = int(line[0].split("[")[1].strip("]"))
            value = (int(line[1]) & andmask) | ormask
            memory[location] = value

    total_in_memory = 0

    for val in memory.values():
        total_in_memory += val

    return total_in_memory

print(part_1())