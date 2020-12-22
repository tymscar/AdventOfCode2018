from math import sqrt

class Tile():
    def __init__(self, tiledef):
        self.id = int(tiledef.split("\n")[0].split(" ")[1].split(":")[0])

        self.data = tiledef.split("\n")[1:]

        self.used = False

        binary_string_array = []
        binary_string_array_flipped = []
        for i in range(10):
            if self.data[0][i] == ".":
                binary_string_array.append("0")
            else:
                binary_string_array.append("1")
            if self.data[0][9 - i] == ".":
                binary_string_array_flipped.append("0")
            else:
                binary_string_array_flipped.append("1")
        self.border_up = [int("".join(binary_string_array), 2), int("".join(binary_string_array_flipped), 2)]

        binary_string_array = []
        binary_string_array_flipped = []
        for i in range(10):
            if self.data[i][9] == ".":
                binary_string_array.append("0")
            else:
                binary_string_array.append("1")
            if self.data[9 - i][9] == ".":
                binary_string_array_flipped.append("0")
            else:
                binary_string_array_flipped.append("1")
        self.border_right = [int("".join(binary_string_array), 2), int("".join(binary_string_array_flipped), 2)]

        binary_string_array = []
        binary_string_array_flipped = []
        for i in range(10):
            if self.data[9][9 - i] == ".":
                binary_string_array.append("0")
            else:
                binary_string_array.append("1")
            if self.data[9][i] == ".":
                binary_string_array_flipped.append("0")
            else:
                binary_string_array_flipped.append("1")
        self.border_down = [int("".join(binary_string_array), 2), int("".join(binary_string_array_flipped), 2)]

        binary_string_array = []
        binary_string_array_flipped = []
        for i in range(10):
            if self.data[9 - i][0] == ".":
                binary_string_array.append("0")
            else:
                binary_string_array.append("1")
            if self.data[i][0] == ".":
                binary_string_array_flipped.append("0")
            else:
                binary_string_array_flipped.append("1")
        self.border_left = [int("".join(binary_string_array), 2), int("".join(binary_string_array_flipped), 2)]

        self.rotation = 0
        self.flip = False

        self.minimap_location = []

    def get_borders(self):
        if self.flip == False:
            if self.rotation == 0:
                up = self.border_up[0]
                right = self.border_right[0]
                down = self.border_down[0]
                left = self.border_left[0]
            elif self.rotation == 90:
                up = self.border_left[0]
                right = self.border_up[0]
                down = self.border_right[0]
                left = self.border_down[0]
            elif self.rotation == 180:
                up = self.border_down[0]
                right = self.border_left[0]
                down = self.border_up[0]
                left = self.border_right[0]
            else:
                up = self.border_right[0]
                right = self.border_down[0]
                down = self.border_left[0]
                left = self.border_up[0]
        else:
            if self.rotation == 0:
                up = self.border_down[1]
                right = self.border_right[1]
                down = self.border_up[1]
                left = self.border_left[1]
            elif self.rotation == 90:
                up = self.border_left[1]
                right = self.border_down[1]
                down = self.border_right[1]
                left = self.border_up[1]
            elif self.rotation == 180:
                up = self.border_up[1]
                right = self.border_left[1]
                down = self.border_down[1]
                left = self.border_right[1]
            else:
                up = self.border_right[1]
                right = self.border_up[1]
                down = self.border_left[1]
                left = self.border_down[1]

        return [up, right, down, left]



def where_fit(parent, kid):
    [parent_up,parent_right,parent_down,parent_left] = parent.get_borders()
    orig_rot = kid.rotation
    orig_flip = kid.flip

    for i in range(4):
        kid.rotation = i * 90
        kid.flip = False
        [kid_up, kid_right, kid_down, kid_left] = kid.get_borders()
        if parent_up == kid_down:
            return [True, False, False, False]
        if parent_right == kid_left:
            return [False, True, False, False]
        if parent_down == kid_up:
            return [False, False, True, False]
        if parent_left == kid_right:
            return [False, False, False, True]

    for i in range(4):
        kid.rotation = i * 90
        kid.flip = True
        [kid_up, kid_right, kid_down, kid_left] = kid.get_borders()
        if parent_up == kid_down:
            return [True, False, False, False]
        if parent_right == kid_left:
            return [False, True, False, False]
        if parent_down == kid_up:
            return [False, False, True, False]
        if parent_left == kid_right:
            return [False, False, False, True]

    kid.rotation = orig_rot
    kid.flip = orig_flip
    return [False, False, False, False]

def part_2():
    tiles = []
    tile_by_name = {}
    corners = []

    for tiledef in open('input.txt').read().split('\n\n'):
        new_tile = Tile(tiledef)
        tiles.append(new_tile)
        tile_by_name[new_tile.id] = new_tile

    rows_and_cols = int(sqrt(len(tiles)))

    for tile in tiles:
        neighbours = 0
        for neighbour in tiles:
            if tile.id != neighbour.id:
                if where_fit(tile, neighbour) != [False, False, False, False]:
                    neighbours += 1
        if neighbours == 2:
            corners.append(tile)

    for corner in corners:
        starting_tile = corner

        for tile in tiles:
            tile.rotation = 0
            tile.flip = False


        minimap = [[None for _ in range(rows_and_cols)] for _ in range(rows_and_cols)]
        minimap[0][0] = starting_tile
        starting_tile.used = True

        for i in range(rows_and_cols):
            for j in range(rows_and_cols):
                if minimap[i][j] == None:
                    parent_one = minimap[i][j-1]
                    pattern_one = [False, True, False, False]
                    parent_two = minimap[i-1][j]
                    pattern_two = [False, False, True, False]
                    for kid in tiles:
                        if kid.used == False:
                            orig_kid_rot = kid.rotation
                            orig_kid_flip = kid.flip
                            if parent_one != None and kid.id != parent_one.id and pattern_one == where_fit(parent_one, kid):
                                minimap[i][j] = kid
                                kid.used = True
                                break
                            else:
                                kid.rotation = orig_kid_rot
                                kid.flip = orig_kid_flip
                            if parent_two != None and kid.id != parent_two.id and pattern_two == where_fit(parent_two,kid):
                                minimap[i][j] = kid
                                kid.used = True
                                break
                            else:
                                kid.rotation = orig_kid_rot
                                kid.flip = orig_kid_flip

        for i in range(rows_and_cols):
            for j in range(rows_and_cols):
                if minimap[i][j] != None:
                    print(minimap[i][j].id, end="|  ")
                else:
                    print("MISSING", end="|  ")
            print()
            print("______________________")

        print("\n\n")


    return "Done"

print(part_2())
