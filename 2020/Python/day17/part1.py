from collections import defaultdict

def get_neighbours(of):
    neighbours = []

    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                if x != 0 or y != 0 or z != 0:
                    neighbours.append((of[0] + x, of[1] + y,of[2] + z))

    return neighbours


def part_1():
    file = open('input.txt', 'r')
    world = defaultdict(lambda: ".")


    y = 0
    for line in file:
        line = line.strip('\n')
        x = 0
        for cube in line:
            world[(x,y,0)] = cube
            x+=1
        y += 1

    cycle = 0
    while cycle < 6:
        new_world = defaultdict(lambda: ".")

        for x in range(0-(cycle+1),x + (cycle+2)):
            for y in range(0 - (cycle+1), y + (cycle+2)):
                for z in range(0-(cycle+1), (cycle+2)):
                    curr_cube = (x,y,z)

                    active_neighbours = 0
                    for neighbor in get_neighbours(curr_cube):
                        if world[neighbor] == "#":
                            active_neighbours += 1
                    if world[curr_cube] == "#":
                        if active_neighbours < 2 or active_neighbours > 3:
                            new_world[curr_cube] = "."
                        else:
                            new_world[curr_cube] = "#"
                    else:
                        if active_neighbours == 3:
                            new_world[curr_cube] = "#"
                        else:
                            new_world[curr_cube] = "."

        world = new_world
        cycle += 1

    active_cubes = 0
    for cube in world:
        if world[cube] == "#":
            active_cubes += 1

    return active_cubes


print(part_1())