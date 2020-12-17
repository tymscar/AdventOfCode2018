from collections import defaultdict

def part_2():
    file = open('input.txt', 'r')
    world_one = defaultdict(lambda: ".")
    world_two = defaultdict(lambda: ".")


    y = 0
    for line in file:
        line = line.strip('\n')
        x = 0
        for cube in line:
            world_one[(x,y,0,0)] = cube
            world_two[(x,y,0,0)] = cube
            x+=1
        y += 1

    minmax_x = [-1, x + 2]
    minmax_y = [-1, y + 2]
    minmax_z = [-1, 2]
    minmax_w = [-1, 2]

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

        for x in range(minmax_x[0], minmax_x[1]):
            for y in range(minmax_y[0], minmax_y[1]):
                for z in range(minmax_z[0], minmax_z[1]):
                    for w in range(minmax_w[0], minmax_w[1]):
                        curr_cube = (x,y,z,w)

                        active_neighbours = 0

                        for a in range(-1, 2):
                            for b in range(-1, 2):
                                for c in range(-1, 2):
                                    for d in range(-1, 2):
                                        if a != 0 or b != 0 or c != 0 or d != 0:
                                            if this_world[(a + x, b + y, c + z, d + w)] == "#":
                                                active_neighbours += 1


                        if this_world[curr_cube] == "#":
                            if active_neighbours < 2 or active_neighbours > 3:
                                that_world[curr_cube] = "."
                            else:
                                that_world[curr_cube] = "#"
                                minmax_x[0] = min(minmax_x[0], curr_cube[0] - 2)
                                minmax_y[0] = min(minmax_y[0], curr_cube[1] - 2)
                                minmax_z[0] = min(minmax_z[0], curr_cube[2] - 2)
                                minmax_w[0] = min(minmax_w[0], curr_cube[3] - 2)
                                minmax_x[1] = max(minmax_x[1], curr_cube[0] + 2)
                                minmax_y[1] = max(minmax_y[1], curr_cube[1] + 2)
                                minmax_z[1] = max(minmax_z[1], curr_cube[2] + 2)
                                minmax_w[1] = max(minmax_w[1], curr_cube[3] + 2)

                        else:
                            if active_neighbours == 3:
                                that_world[curr_cube] = "#"
                                minmax_x[0] = min(minmax_x[0], curr_cube[0] - 2)
                                minmax_y[0] = min(minmax_y[0], curr_cube[1] - 2)
                                minmax_z[0] = min(minmax_z[0], curr_cube[2] - 2)
                                minmax_w[0] = min(minmax_w[0], curr_cube[3] - 2)
                                minmax_x[1] = max(minmax_x[1], curr_cube[0] + 2)
                                minmax_y[1] = max(minmax_y[1], curr_cube[1] + 2)
                                minmax_z[1] = max(minmax_z[1], curr_cube[2] + 2)
                                minmax_w[1] = max(minmax_w[1], curr_cube[3] + 2)
                            else:
                                that_world[curr_cube] = "."


        cycle += 1

    if curr_world_num == 1:
        this_world = world_two
    else:
        this_world = world_one

    active_cubes = 0
    for cube in this_world:
        if this_world[cube] == "#":
            active_cubes += 1

    return active_cubes


print(part_2())