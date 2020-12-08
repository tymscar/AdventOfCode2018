class Instruction:
    def __init__(self, name, amount):
        self.name = name
        self.amount = int(amount)


def find_potential_problems(memory):
    potentials = []

    memory_pointer = 0

    visited = {}

    while memory_pointer not in visited:
        visited[memory_pointer] = True
        curr = memory[memory_pointer]
        
        if curr.name == "nop":
            potentials.append(memory_pointer)
        
        if curr.name != "jmp":
            memory_pointer += 1
        else:
            potentials.append(memory_pointer)
            memory_pointer += curr.amount
            
    return potentials


def run(memory, index_to_change):
    accumulator = 0
    memory_pointer = 0

    visited = {}


    while memory_pointer not in visited and memory_pointer < len(memory):
        visited[memory_pointer] = True
        curr_name = memory[memory_pointer].name
        curr_amount = memory[memory_pointer].amount

        if memory_pointer == index_to_change:
            if curr_name == "nop":
                curr_name = "jmp"
            else:
                curr_name = "nop"

        if curr_name == "nop":
            memory_pointer += 1
        elif curr_name == "acc":
            accumulator += curr_amount
            memory_pointer += 1
        else:
            memory_pointer += curr_amount

    if memory_pointer >= len(memory):
        return accumulator
    else:
        return -999999


def part_2():
    file = open('input.txt', 'r')

    memory = []


    for line in file:
        line = line.strip("\n")
        new_instruction = Instruction(line.split(sep=" ")[0], line.split(sep=" ")[1])
        memory.append(new_instruction)

    problems = find_potential_problems(memory)

    for problem in problems:
        curr = run(memory, problem)
        if curr != -999999:
            return curr

    return "Impossible to solve"

print(part_2())