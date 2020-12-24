class Tile():
    def __init__(self, pos):
        self.white = True
        self.pos = pos

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

def part_1():
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

    black_tiles = 0

    for coord in tiles:
        if tiles[coord].white == False:
            black_tiles += 1


    return black_tiles

print(part_1())