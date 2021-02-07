class Tile():
    def __init__(self, pos):
        self.white = True
        self.pos = pos
        self.will_flip = False

    def get_neighbour_coords(self):
        neighbours = []

        neighbours.append((self.pos[0], self.pos[1] + 1))
        neighbours.append((self.pos[0] + 1, self.pos[1]))
        neighbours.append((self.pos[0] + 1, self.pos[1] - 1))
        neighbours.append((self.pos[0], self.pos[1] - 1))
        neighbours.append((self.pos[0] - 1, self.pos[1]))
        neighbours.append((self.pos[0] - 1, self.pos[1] + 1))

        return neighbours

    def flip(self):
        self.white = not self.white

def get_new_coord(from_tile, instructions):
    curr = [from_tile.pos[0], from_tile.pos[1]]
    for instruction in instructions:
        if instruction == "ne":
            curr[1] += 1
        elif instruction == "e":
            curr[0] += 1
        elif instruction == "se":
            curr[0] += 1
            curr[1] -= 1
        elif instruction == "sw":
            curr[1] -= 1
        elif instruction == "w":
            curr[0] -= 1
        elif instruction == "nw":
            curr[0] -= 1
            curr[1] += 1
    return (curr[0], curr[1])

def part_2():
    file = open('input.txt', 'r')
    tiles = {}
    starting_tile = Tile((0,0))
    tiles[starting_tile.pos] = starting_tile

    for line in file:
        line = line.strip("\n")
        instructions_on_line = []
        index = 0
        while index < len(line):
            if line[index] == "w" or line[index] == "e":
                instructions_on_line.append(line[index])
            else:
                if line[index+1] == "w" or line[index+1] == "e":
                    instructions_on_line.append(line[index:index+2])
                    index += 1
                else:
                    instructions_on_line.append(line[index])
            index += 1

        line_coord = get_new_coord(starting_tile,instructions_on_line)
        if line_coord in tiles:
            tiles[line_coord].flip()
        else:
            new_tile = Tile(line_coord)
            new_tile.flip()
            tiles[line_coord] = new_tile



    for day in range(100):
        to_be_added = []
        for coord in tiles:
            black_adj_tiles = 0
            for neighbour_coord in tiles[coord].get_neighbour_coords():
                if neighbour_coord not in tiles:
                    new_tile = Tile(neighbour_coord)
                    to_be_added.append(new_tile)
                else:
                    if tiles[neighbour_coord].white == False:
                        black_adj_tiles += 1
            if tiles[coord].white == True:
                if black_adj_tiles == 2:
                    tiles[coord].will_flip = True
            if tiles[coord].white == False:
                if black_adj_tiles == 0 or black_adj_tiles > 2:
                    tiles[coord].will_flip = True

        for tile in to_be_added:
            black_adj_tiles = 0
            for neighbour_coord in tile.get_neighbour_coords():
                if neighbour_coord in tiles:
                    if tiles[neighbour_coord].white == False:
                        black_adj_tiles += 1

            if black_adj_tiles == 2:
                tile.flip()


        for coord in tiles:
            if tiles[coord].will_flip == True:
                tiles[coord].will_flip = False
                tiles[coord].flip()
        for tile in to_be_added:
            tiles[tile.pos] = tile




    black_tiles = 0

    for coord in tiles:
        if tiles[coord].white == False:
            black_tiles += 1


    return black_tiles

print(part_2())