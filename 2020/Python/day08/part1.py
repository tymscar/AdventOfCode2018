class Instruction:
    def __init__(self, name, amount):
        self.name = name
        self.amount = int(amount)


def part_1():
    file = open('input.txt', 'r')

    memory = []

    accumulator = 0
    memory_pointer = 0

    visited = {}

    for line in file:
        line = line.strip("\n")
        new_instruction = Instruction(line.split(sep=" ")[0], line.split(sep=" ")[1])
        memory.append(new_instruction)

    while memory_pointer not in visited:
        visited[memory_pointer] = True
        curr = memory[memory_pointer]
        if curr.name == "nop":
            memory_pointer += 1
        elif curr.name == "acc":
            accumulator += curr.amount
            memory_pointer += 1
        else:
            memory_pointer += curr.amount

    return accumulator


print(part_1())