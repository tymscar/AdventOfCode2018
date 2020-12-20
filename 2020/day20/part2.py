class Tile():
    def __init__(self, tiledef):
        self.id = int(tiledef.split("\n")[0].split(" ")[1].split(":")[0])

        self.data = tiledef.split("\n")[1:]

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

        self.top = None
        self.right = None
        self.bot = None
        self.left = None
        self.flipped = False
        self.rotation = 0

        self.fixed = False
        self.placed = False
        self.neighbours = []

    def get_border_north(self, flipped):
        if flipped:
            if self.rotation == 0:
                return self.border_down[1]
            elif self.rotation == 90:
                return self.border_left[1]
            elif self.rotation == 180:
                return self.border_up[1]
            else:
                return self.border_right[1]
        else:
            if self.rotation == 0:
                return self.border_up[0]
            elif self.rotation == 90:
                return self.border_left[0]
            elif self.rotation == 180:
                return self.border_down[0]
            else:
                return self.border_right[0]

    def get_border_east(self, flipped):
        if flipped:
            if self.rotation == 0:
                return self.border_right[1]
            elif self.rotation == 90:
                return self.border_down[1]
            elif self.rotation == 180:
                return self.border_left[1]
            else:
                return self.border_up[1]
        else:
            if self.rotation == 0:
                return self.border_right[0]
            elif self.rotation == 90:
                return self.border_up[0]
            elif self.rotation == 180:
                return self.border_left[0]
            else:
                return self.border_down[0]

    def get_border_south(self, flipped):
        if flipped:
            if self.rotation == 0:
                return self.border_up[1]
            elif self.rotation == 90:
                return self.border_right[1]
            elif self.rotation == 180:
                return self.border_down[1]
            else:
                return self.border_left[1]
        else:
            if self.rotation == 0:
                return self.border_down[0]
            elif self.rotation == 90:
                return self.border_right[0]
            elif self.rotation == 180:
                return self.border_up[0]
            else:
                return self.border_left[0]

    def get_border_west(self, flipped):
        if flipped:
            if self.rotation == 0:
                return self.border_left[1]
            elif self.rotation == 90:
                return self.border_up[1]
            elif self.rotation == 180:
                return self.border_right[1]
            else:
                return self.border_down[1]
        else:
            if self.rotation == 0:
                return self.border_left[0]
            elif self.rotation == 90:
                return self.border_down[0]
            elif self.rotation == 180:
                return self.border_right[0]
            else:
                return self.border_up[0]

    def generate_neighbours(self):
        if self.top != None:
            self.neighbours.append(self.top)
        if self.right != None:
            self.neighbours.append(self.right)
        if self.bot != None:
            self.neighbours.append(self.bot)
        if self.left != None:
            self.neighbours.append(self.left)

        self.top = None
        self.right = None
        self.bot = None
        self.left = None

    def number_of_empty_neighbours(self):
        return 4 - len(self.neighbours)


def part_2():
    tiles = []

    for tiledef in open('input.txt').read().split('\n\n'):
        new_tile = Tile(tiledef)
        tiles.append(new_tile)

    queue = [tiles[0]]
    while len(queue) > 0:
        curr_tile = queue.pop(0)
        if curr_tile.placed != True:
            curr_tile.placed = True
            for possible_adj_tile in tiles:
                if possible_adj_tile.id != curr_tile.id:
                    top = curr_tile.border_up[0]  # try top
                    if top == possible_adj_tile.border_up[0] or top == possible_adj_tile.border_up[1]:
                        curr_tile.top = possible_adj_tile
                        possible_adj_tile.top = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if top == possible_adj_tile.border_right[0] or top == possible_adj_tile.border_right[1]:
                        curr_tile.top = possible_adj_tile
                        possible_adj_tile.right = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if top == possible_adj_tile.border_down[0] or top == possible_adj_tile.border_down[1]:
                        curr_tile.top = possible_adj_tile
                        possible_adj_tile.bot = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if top == possible_adj_tile.border_left[0] or top == possible_adj_tile.border_left[1]:
                        curr_tile.top = possible_adj_tile
                        possible_adj_tile.left = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)

                    right = curr_tile.border_right[0]  # try right
                    if right == possible_adj_tile.border_up[0] or right == possible_adj_tile.border_up[1]:
                        curr_tile.right = possible_adj_tile
                        possible_adj_tile.top = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if right == possible_adj_tile.border_right[0] or right == possible_adj_tile.border_right[1]:
                        curr_tile.right = possible_adj_tile
                        possible_adj_tile.right = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if right == possible_adj_tile.border_down[0] or right == possible_adj_tile.border_down[1]:
                        curr_tile.right = possible_adj_tile
                        possible_adj_tile.bot = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if right == possible_adj_tile.border_left[0] or right == possible_adj_tile.border_left[1]:
                        curr_tile.right = possible_adj_tile
                        possible_adj_tile.left = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)

                    bot = curr_tile.border_down[0]  # try bot
                    if bot == possible_adj_tile.border_up[0] or bot == possible_adj_tile.border_up[1]:
                        curr_tile.bot = possible_adj_tile
                        possible_adj_tile.top = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if bot == possible_adj_tile.border_right[0] or bot == possible_adj_tile.border_right[1]:
                        curr_tile.bot = possible_adj_tile
                        possible_adj_tile.right = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if bot == possible_adj_tile.border_down[0] or bot == possible_adj_tile.border_down[1]:
                        curr_tile.bot = possible_adj_tile
                        possible_adj_tile.bot = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if bot == possible_adj_tile.border_left[0] or bot == possible_adj_tile.border_left[1]:
                        curr_tile.bot = possible_adj_tile
                        possible_adj_tile.left = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)

                    left = curr_tile.border_left[0]  # try left
                    if left == possible_adj_tile.border_up[0] or left == possible_adj_tile.border_up[1]:
                        curr_tile.left = possible_adj_tile
                        possible_adj_tile.top = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if left == possible_adj_tile.border_right[0] or left == possible_adj_tile.border_right[1]:
                        curr_tile.left = possible_adj_tile
                        possible_adj_tile.right = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if left == possible_adj_tile.border_down[0] or left == possible_adj_tile.border_down[1]:
                        curr_tile.left = possible_adj_tile
                        possible_adj_tile.bot = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)
                    if left == possible_adj_tile.border_left[0] or left == possible_adj_tile.border_left[1]:
                        curr_tile.left = possible_adj_tile
                        possible_adj_tile.left = curr_tile
                        if possible_adj_tile.placed == False:
                            queue.append(possible_adj_tile)

    answer = 1

    for tile in tiles:
        tile.generate_neighbours()
        # print(f"{tile.id} has these neighs: {tile.neighbours}")
        if tile.number_of_empty_neighbours() == 2:
            answer *= tile.id
            starting_point = tile


    queue = [starting_point]
    starting_point.fixed = True
    while len(queue) > 0:
        curr_tile = queue.pop(0)
        for neighbour in curr_tile.neighbours:
            if neighbour.fixed == False:
                top = curr_tile.get_border_north(curr_tile.flipped)  # try top
                if top == neighbour.get_border_north(True) or top == neighbour.get_border_north(False):
                    if top == neighbour.get_border_north(False):
                        neighbour.rotation = 180
                    else:
                        neighbour.rotation = 0
                        neighbour.flipped = True
                    curr_tile.top = neighbour
                    neighbour.bot = curr_tile
                    #print(f"{neighbour.id} added to other node")
                if top == neighbour.get_border_east(True) or top == neighbour.get_border_east(False):
                    if top == neighbour.get_border_east(False):
                        neighbour.rotation = 90
                    else:
                        neighbour.rotation = 90
                        neighbour.flipped = True
                    curr_tile.top = neighbour
                    neighbour.bot = curr_tile
                if top == neighbour.get_border_south(True) or top == neighbour.get_border_south(False):
                    if top == neighbour.get_border_south(False):
                        neighbour.rotation = 0
                    else:
                        neighbour.rotation = 180
                        neighbour.flipped = True
                    curr_tile.top = neighbour
                    neighbour.bot = curr_tile
                if top == neighbour.get_border_west(True) or top == neighbour.get_border_west(False):
                    if top == neighbour.get_border_west(False):
                        neighbour.rotation = 270
                    else:
                        neighbour.rotation = 270
                        neighbour.flipped = True
                    curr_tile.top = neighbour
                    neighbour.bot = curr_tile

                right = curr_tile.get_border_east(curr_tile.flipped)  # try right
                if right == neighbour.get_border_north(True) or right == neighbour.get_border_north(False):
                    if right == neighbour.get_border_north(False):
                        neighbour.rotation = 270
                    else:
                        neighbour.rotation = 90
                        neighbour.flipped = True
                    curr_tile.right = neighbour
                    neighbour.left = curr_tile
                if right == neighbour.get_border_east(True)  or right == neighbour.get_border_east(False):
                    if right == neighbour.get_border_east(False):
                        neighbour.rotation = 180
                    else:
                        neighbour.rotation = 180
                        neighbour.flipped = True
                    curr_tile.right = neighbour
                    neighbour.left = curr_tile
                if right == neighbour.get_border_south(True) or right == neighbour.get_border_south(False):
                    if right == neighbour.get_border_south(False):
                        neighbour.rotation = 90
                    else:
                        neighbour.rotation = 270
                        neighbour.flipped = True
                    curr_tile.right = neighbour
                    neighbour.left = curr_tile
                if right == neighbour.get_border_west(True) or right == neighbour.get_border_west(False):
                    if right == neighbour.get_border_west(False):
                        neighbour.rotation = 0
                    else:
                        neighbour.rotation = 0
                        neighbour.flipped = True
                    curr_tile.right = neighbour
                    neighbour.left = curr_tile

                bot = curr_tile.get_border_south(curr_tile.flipped)  # try bot
                if bot == neighbour.get_border_north(True) or bot == neighbour.get_border_north(False):
                    if bot == neighbour.get_border_north(False):
                        neighbour.rotation = 0
                    else:
                        neighbour.rotation = 180
                        neighbour.flipped = True
                    curr_tile.bot = neighbour
                    neighbour.top = curr_tile
                if bot == neighbour.get_border_east(True) or bot == neighbour.get_border_east(False):
                    if bot == neighbour.get_border_east(False):
                        neighbour.rotation = 270
                    else:
                        neighbour.rotation = 270
                        neighbour.flipped = True
                    curr_tile.bot = neighbour
                    neighbour.top = curr_tile
                if bot == neighbour.get_border_south(True) or bot == neighbour.get_border_south(False):
                    if bot == neighbour.get_border_south(False):
                        neighbour.rotation = 180
                    else:
                        neighbour.rotation = 0
                        neighbour.flipped = True
                    curr_tile.bot = neighbour
                    neighbour.top = curr_tile
                if bot == neighbour.get_border_west(True) or bot == neighbour.get_border_west(False):
                    if bot == neighbour.get_border_west(False):
                        neighbour.rotation = 90
                    else:
                        neighbour.rotation = 90
                        neighbour.flipped = True
                    curr_tile.bot = neighbour
                    neighbour.top = curr_tile

                left = curr_tile.get_border_west(curr_tile.flipped) # try left
                if left == neighbour.get_border_north(True) or left == neighbour.get_border_north(False):
                    if left == neighbour.get_border_north(False):
                        neighbour.rotation = 90
                    else:
                        neighbour.rotation = 270
                        neighbour.flipped = True
                    curr_tile.left = neighbour
                    neighbour.right = curr_tile
                if left == neighbour.get_border_east(True) or left == neighbour.get_border_east(False):
                    if left == neighbour.get_border_east(False) :
                        neighbour.rotation = 0
                    else:
                        neighbour.rotation = 0
                        neighbour.flipped = True
                    curr_tile.left = neighbour
                    neighbour.right = curr_tile
                if left == neighbour.get_border_south(True) or left == neighbour.get_border_south(False):
                    if left == neighbour.get_border_south(False):
                        neighbour.rotation = 270
                    else:
                        neighbour.rotation = 90
                        neighbour.flipped = True
                    curr_tile.left = neighbour
                    neighbour.right = curr_tile
                if left == neighbour.get_border_west(True) or left == neighbour.get_border_west(False):
                    if left == neighbour.get_border_west(False):
                        neighbour.rotation = 180
                    else:
                        neighbour.rotation = 180
                        neighbour.flipped = True
                    curr_tile.left = neighbour
                    neighbour.right = curr_tile

                neighbour.fixed = True
                #print(f"finished {neighbour.id}")
                queue.append(neighbour)




    print("\n\n\n\n\n")
    for tile in tiles:
        #if tile.id == 1951:
            for nei in tile.neighbours:

                if nei.get_border_north(nei.flipped) == tile.get_border_south(tile.flipped):
                    nei.top = tile
                    tile.bot = nei
                    print(f"{tile.id}: {nei.id} is on top")
                if nei.get_border_south(nei.flipped) == tile.get_border_north(tile.flipped):
                    nei.bot = tile
                    tile.top = nei
                    print(f"{tile.id}: {nei.id} is on bot")
                if nei.get_border_west(nei.flipped) == tile.get_border_east(tile.flipped):
                    nei.left = tile
                    tile.right = nei
                    print(f"{tile.id}: {nei.id} is on left")
                if nei.get_border_east(nei.flipped) == tile.get_border_west(tile.flipped):
                    nei.right = tile
                    tile.left = nei
                    print(f"{tile.id}: {nei.id} is on right")
            print("")



    return answer

print(part_2())
