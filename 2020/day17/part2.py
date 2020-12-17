from collections import defaultdict

def get_neighbours(of):
    neighbours = []

    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for w in range(-1,2):
                    if x != 0 or y != 0 or z != 0 or w != 0:
                        neighbours.append((of[0] + x, of[1] + y,of[2] + z, of[3] + w))

    return neighbours


def part_2():
    file = open('input.txt', 'r')
    world_one = defaultdict(lambda: ".")
    world_two = defaultdict(lambda: ".")

    #neighbours = {}

    y = 0
    for line in file:
        line = line.strip('\n')
        x = 0
        for cube in line:
            world_one[(x,y,0,0)] = cube
            world_two[(x,y,0,0)] = cube
            x+=1
        y += 1

    cycle = 0
    curr_world_num = 1
    while cycle < 6:
        if curr_world_num == 1:
            this_world = world_two
            that_world = world_one
            curr_world_num = 2
        else:
            that_world = world_two
            this_world = world_one
            curr_world_num = 1

        for x in range(0-(cycle+1), x + (cycle+2)):
            for y in range(0 - (cycle+1), y + (cycle+2)):
                for z in range(0-(cycle+1), (cycle+2)):
                    for w in range(0-(cycle+1), (cycle+2)):
                        curr_cube = (x,y,z,w)

                        active_neighbours = 0
                        #if curr_cube in neighbours:
                        #    neighs = neighbours[curr_cube]
                        #else:
                        #    neighs = get_neighbours(curr_cube)
                        #    neighbours[curr_cube] = neighs
                        for neighbor in get_neighbours(curr_cube):
                            if this_world[neighbor] == "#":
                                active_neighbours += 1
                        if this_world[curr_cube] == "#":
                            if active_neighbours < 2 or active_neighbours > 3:
                                that_world[curr_cube] = "."
                            else:
                                that_world[curr_cube] = "#"
                        else:
                            if active_neighbours == 3:
                                that_world[curr_cube] = "#"
                            else:
                                that_world[curr_cube] = "."


        cycle += 1

    if curr_world_num == 1:
        this_world = world_two
        that_world = world_one
        curr_world_num = 2
    else:
        that_world = world_two
        this_world = world_one
        curr_world_num = 1

    active_cubes = 0
    for cube in this_world:
        if this_world[cube] == "#":
            active_cubes += 1

    return active_cubes


print(part_2())