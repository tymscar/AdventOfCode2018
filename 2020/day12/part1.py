class Ship():
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.rot = 0

    def get_facing_direction(self):
        if self.rot == 0:
            return "E"
        if self.rot == 1:
            return "S"
        if self.rot == 2:
            return "W"
        return "N"
            

    def move(self,direction, how_much):
        if direction == "F":
            direction = self.get_facing_direction()

        if direction == "E":
            self.pos_x += how_much
        if direction == "S":
            self.pos_y -= how_much
        if direction == "W":
            self.pos_x -= how_much
        if direction == "N":
            self.pos_y += how_much

    def rotate(self, direction, how_much):
        if direction == "R":
            self.rot += how_much//90
        if direction == "L":
            self.rot -= how_much//90
        self.rot = self.rot%4

    def get_manhattan_distance_from_base(self):
        return abs(self.pos_x)+ abs(self.pos_y)

def part_1():
    file = open('input.txt', 'r')
    ship = Ship()

    for line in file:
        line = line.strip("\n")
        instruction = line[0]
        quantity = int(line[1:])
        if instruction in ["R","L"]:
            ship.rotate(instruction,quantity)
        else:
            ship.move(instruction,quantity)


    return ship.get_manhattan_distance_from_base()

print(part_1())
