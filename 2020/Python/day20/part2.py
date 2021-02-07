from math import sqrt

class Photo():
    def __init__(self, size):
        self.data = [[0 for _ in range(size * 8)] for _ in range(size *  8)]
        self.size = size * 8

    def flip(self):
        new_data = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                new_data[i][j] = self.data[i][self.size-1-j]

        self.data = new_data

    def rotate(self):
        new_data = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for j in range(self.size):
            for i in range(self.size-1,-1,-1):
                new_data[j][self.size-1-i] = self.data[i][j]

        self.data = new_data

    def how_many_nessie(self):
        nessies = 0
        for i in range(2,self.size):
            for j in range(0, self.size - 19):
                if self.data[i-1][j] == "#" and self.data[i][j+1] == "#" and self.data[i][j+4] == "#" and self.data[i-1][j+5] == "#" and self.data[i-1][j+6] == "#" and self.data[i][j+7] == "#" and self.data[i][j+10] == "#" and self.data[i-1][j+11] == "#" and self.data[i-1][j+12] == "#" and self.data[i][j+13] == "#" and self.data[i][j+16] == "#" and self.data[i-1][j+17] == "#" and self.data[i-1][j+18] == "#" and self.data[i-2][j+18] == "#" and self.data[i-1][j+19] == "#":
                    nessies += 1

        return nessies

    def how_many_rough_waters(self):
        rough_waters = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] == "#":
                    rough_waters += 1
        return rough_waters


    def how_many_nessies_on_any_side(self):
        nessies = self.how_many_nessie()
        if nessies > 0:
            return nessies
        self.rotate()
        nessies = self.how_many_nessie()
        if nessies > 0:
            return nessies
        self.rotate()
        nessies = self.how_many_nessie()
        if nessies > 0:
            return nessies
        self.rotate()
        nessies = self.how_many_nessie()
        if nessies > 0:
            return nessies
        self.flip()
        nessies = self.how_many_nessie()
        if nessies > 0:
            return nessies
        self.rotate()
        nessies = self.how_many_nessie()
        if nessies > 0:
            return nessies
        self.rotate()
        nessies = self.how_many_nessie()
        if nessies > 0:
            return nessies
        self.rotate()
        nessies = self.how_many_nessie()
        if nessies > 0:
            return nessies
        self.rotate()
        nessies = self.how_many_nessie()
        if nessies > 0:
            return nessies


class Tile():
    def __init__(self, tiledef):
        self.id = int(tiledef.split("\n")[0].split(" ")[1].split(":")[0])

        self.data = tiledef.split("\n")[1:]
        self.generate_borders()

        self.pos = (0,0)

        self.neighbours = []

        self.placed = False


    def generate_borders(self):
        binary_array = []
        for j in range(10):
            if self.data[0][j] == "#":
                binary_array.append("1")
            else:
                binary_array.append("0")
        self.border_up = int("".join(binary_array), 2)

        binary_array = []
        for i in range(10):
            if self.data[i][9] == "#":
                binary_array.append("1")
            else:
                binary_array.append("0")
        self.border_right = int("".join(binary_array), 2)

        binary_array = []
        for j in range(10):
            if self.data[9][j] == "#":
                binary_array.append("1")
            else:
                binary_array.append("0")
        self.border_down = int("".join(binary_array), 2)

        binary_array = []
        for i in range(10):
            if self.data[i][0] == "#":
                binary_array.append("1")
            else:
                binary_array.append("0")
        self.border_left = int("".join(binary_array), 2)

    def flip(self):
        new_data = [[0 for _ in range(10)] for _ in range(10)]
        for i in range(10):
            for j in range(10):
                new_data[i][j] = self.data[i][9-j]

        self.data = new_data
        self.generate_borders()

    def rotate(self):
        new_data = [[0 for _ in range(10)] for _ in range(10)]
        for j in range(10):
            for i in range(9,-1,-1):
                new_data[j][9-i] = self.data[i][j]

        self.data = new_data
        self.generate_borders()


    def print(self):
        for i in range(10):
            for j in range(10):
                print(self.data[i][j],end=" ")
            print()
        print("\n\n")

def where_to_fit_one_orientation(parent, kid):
    up = False
    right = False
    down = False
    left = False

    if parent.border_up == kid.border_down:
        up = True
        return [up, right, down, left]

    if parent.border_right == kid.border_left:
        right = True
        return [up, right, down, left]

    if parent.border_down == kid.border_up:
        down = True
        return [up, right, down, left]

    if parent.border_left == kid.border_right:
        left = True
        return [up, right, down, left]

    return [up, right, down, left]

def where_to_fit(parent, kid):
    no_fit = [False, False, False, False]

    if where_to_fit_one_orientation(parent, kid) != no_fit:
        return where_to_fit_one_orientation(parent, kid)
    kid.rotate()
    if where_to_fit_one_orientation(parent, kid) != no_fit:
        return where_to_fit_one_orientation(parent, kid)
    kid.rotate()
    if where_to_fit_one_orientation(parent, kid) != no_fit:
        return where_to_fit_one_orientation(parent, kid)
    kid.rotate()
    if where_to_fit_one_orientation(parent, kid) != no_fit:
        return where_to_fit_one_orientation(parent, kid)
    kid.flip()
    if where_to_fit_one_orientation(parent, kid) != no_fit:
        return where_to_fit_one_orientation(parent, kid)
    kid.rotate()
    if where_to_fit_one_orientation(parent, kid) != no_fit:
        return where_to_fit_one_orientation(parent, kid)
    kid.rotate()
    if where_to_fit_one_orientation(parent, kid) != no_fit:
        return where_to_fit_one_orientation(parent, kid)
    kid.rotate()
    if where_to_fit_one_orientation(parent, kid) != no_fit:
        return where_to_fit_one_orientation(parent, kid)

    return no_fit

def part_2():
    tiles = []
    tile_by_name = {}

    for tiledef in open('input.txt').read().split('\n\n'):
        new_tile = Tile(tiledef)
        tiles.append(new_tile)
        tile_by_name[new_tile.id] = new_tile

    rows_and_cols = int(sqrt(len(tiles)))

    initialmap = [[0 for _ in range(rows_and_cols)] for _ in range(rows_and_cols)]
    photo = Photo(rows_and_cols)

    for tile in tiles:
        for neighbour in tiles:
            if tile.id != neighbour.id and where_to_fit(tile,neighbour) != [False, False, False, False]:
                tile.neighbours.append(neighbour)
        if len(tile.neighbours) == 2:
            starting_piece = tile


    starting_piece.placed = True
    queue = [starting_piece]
    while len(queue) > 0:
        curr_tile = queue.pop(0)
        for neighbour in curr_tile.neighbours:
            if neighbour.placed == False:
                where_does_neighbour_fit = where_to_fit(curr_tile, neighbour)
                if where_does_neighbour_fit[0] == True:
                    neighbour.pos = (curr_tile.pos[0] + 1, curr_tile.pos[1])
                elif where_does_neighbour_fit[1] == True:
                    neighbour.pos = (curr_tile.pos[0], curr_tile.pos[1] + 1)
                elif where_does_neighbour_fit[2] == True:
                    neighbour.pos = (curr_tile.pos[0] - 1, curr_tile.pos[1])
                elif where_does_neighbour_fit[3] == True:
                    neighbour.pos = (curr_tile.pos[0], curr_tile.pos[1] - 1)
                neighbour.placed = True
                queue.append(neighbour)

    minx = 9999
    miny = 9999
    maxx = -9999
    maxy = -9999
    for tile in tiles:
        minx = min(minx, tile.pos[1])
        miny = min(miny, tile.pos[0])
        maxx = max(maxx, tile.pos[1])
        maxy = max(maxy, tile.pos[0])

    if minx < 0:
        compensate_min_x = 0 - minx
    else:
        compensate_min_x = 0
    if miny < 0:
        compensate_min_y = 0 - miny
    else:
        compensate_min_y = 0

    if maxx >= rows_and_cols:
        compensate_max_x = (maxx - rows_and_cols) + 1
    else:
        compensate_max_x = 0
    if maxy >= rows_and_cols:
        compensate_max_y = (maxy - rows_and_cols) + 1
    else:
        compensate_max_y = 0

    for tile in tiles:
        tile.pos = (tile.pos[0] + compensate_min_y - compensate_max_y, tile.pos[1] + compensate_min_x - compensate_max_x)
        initialmap[tile.pos[0]][tile.pos[1]] = tile



    photo_x = 0
    photo_y = 0
    for i in range(rows_and_cols):
        for inner_i in range(8, 0, -1):
            for j in range(rows_and_cols):
                for inner_j in range(1, 9):
                    photo.data[photo_x][photo_y] = initialmap[i][j].data[inner_i][inner_j]
                    photo_y += 1
            photo_x += 1
            photo_y = 0




    return photo.how_many_rough_waters() - (photo.how_many_nessies_on_any_side() * 15)


print(part_2())
