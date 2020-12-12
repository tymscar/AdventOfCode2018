class Waypoint():
    def __init__(self):
        self.pos_x = 10
        self.pos_y = 1

    def move(self, direction, how_much):
        if direction == "E":
            self.pos_x += how_much
        if direction == "S":
            self.pos_y -= how_much
        if direction == "W":
            self.pos_x -= how_much
        if direction == "N":
            self.pos_y += how_much


    def rotate(self, direction, how_much):
        if direction == "L":
            if how_much == 90:
                self.pos_x, self.pos_y = -self.pos_y, self.pos_x
            elif how_much == 180:
                self.pos_x, self.pos_y = -self.pos_x, -self.pos_y
            elif how_much == 270:
                self.pos_x, self.pos_y = self.pos_y, -self.pos_x
        else:
            if how_much == 90:
                self.pos_x, self.pos_y = self.pos_y, -self.pos_x
            elif how_much == 180:
                self.pos_x, self.pos_y = -self.pos_x, -self.pos_y
            elif how_much == 270:
                self.pos_x, self.pos_y = -self.pos_y, self.pos_x


class Ship():
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.way = Waypoint()


    def move(self, direction, how_much):
        if direction == "F":
            self.pos_x += self.way.pos_x * how_much
            self.pos_y += self.way.pos_y * how_much
        else:
            self.way.move(direction, how_much)


    def rotate(self, direction, how_much):
        self.way.rotate(direction, how_much)

    def get_manhattan_distance_from_base(self):
        return abs(self.pos_x) + abs(self.pos_y)


def part_2():
    file = open('input.txt', 'r')
    ship = Ship()

    for line in file:
        line = line.strip("\n")
        instruction = line[0]
        quantity = int(line[1:])
        if instruction in ["R", "L"]:
            ship.rotate(instruction, quantity)
        else:
            ship.move(instruction, quantity)

    return ship.get_manhattan_distance_from_base()


print(part_2())
