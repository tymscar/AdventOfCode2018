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
            if self.data[0][9-i] == ".":
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
            if self.data[9-i][9] == ".":
                binary_string_array_flipped.append("0")
            else:
                binary_string_array_flipped.append("1")
        self.border_right = [int("".join(binary_string_array), 2), int("".join(binary_string_array_flipped), 2)]

        binary_string_array = []
        binary_string_array_flipped = []
        for i in range(10):
            if self.data[9][9-i] == ".":
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
            if self.data[9-i][0] == ".":
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

        self.placed = False

    def number_of_empty_neighbours(self):
        empty_neighbours = 0

        if self.top == None:
            empty_neighbours += 1
        if self.right == None:
            empty_neighbours += 1
        if self.bot == None:
            empty_neighbours += 1
        if self.left == None:
            empty_neighbours += 1

        return empty_neighbours


def part_1():
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
        if tile.number_of_empty_neighbours() == 2:
            answer *= tile.id


    return answer

print(part_1())