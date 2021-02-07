class Seat():
    def __init__(self):
        self.occupied = False
        self.next_state_occupied = False
        self.neighbours = []

def get_neighbours(minimap, posy, posx):
    neighbours = []

    # up
    for i in range(1, len(minimap)):
        if (posy - i) >= 0 and minimap[posy - i][posx] != None:
            neighbours.append((posy - i, posx))
            break

    # up right
    for i in range(1, len(minimap[0])):
        if (posy - i) >= 0 and (posx + i) < len(minimap[0]) and minimap[posy - i][posx + i] != None:
            neighbours.append((posy - i, posx + i))
            break

    # right
    for i in range(1, len(minimap[0])):
        if (posx + i) < len(minimap[0]) and minimap[posy][posx + i] != None:
            neighbours.append((posy, posx + i))
            break

    # down right
    for i in range(1, len(minimap) + len(minimap[0])):
        if (posy + i) < len(minimap) and (posx + i) < len(minimap[0]) and minimap[posy + i][posx + i] != None:
            neighbours.append((posy + i, posx + i))
            break

    # down
    for i in range(1, len(minimap)):
        if (posy + i) < len(minimap) and minimap[posy + i][posx] != None:
            neighbours.append((posy + i, posx))
            break

    # down left
    for i in range(1, len(minimap)):
        if (posy + i) < len(minimap) and (posx - i) >= 0 and minimap[posy + i][posx - i] != None:
            neighbours.append((posy + i, posx - i))
            break

    # left
    for i in range(1, len(minimap[0])):
        if (posx - i) >= 0 and minimap[posy][posx - i] != None:
            neighbours.append((posy, posx - i))
            break

    # up left
    for i in range(1, len(minimap) + len(minimap[0])):
        if (posy - i) >= 0 and (posx - i) >= 0 and minimap[posy - i][posx - i] != None:
            neighbours.append((posy - i, posx - i))
            break

    return neighbours


def part_2():
    file = open('input.txt', 'r')

    minimap = []

    # Create the minimap with the seat objects
    for line in file:
        line = line.strip("\n")
        line_in_map = []
        for char in line:
            if char == "L":
                line_in_map.append(Seat())
            else:
                line_in_map.append(None)
        minimap.append(line_in_map)

    # Populate the neighbours list of each seat for faster access
    for i in range(len(minimap)):
        for j in range(len(minimap[0])):
            if minimap[i][j] != None:
                minimap[i][j].neighbours = get_neighbours(minimap, i, j)

    changes = True

    while changes:
        changes = False
        for i in range(len(minimap)):
            for j in range(len(minimap[0])):
                if minimap[i][j] != None:
                    curr_seat = minimap[i][j]
                    if curr_seat.occupied == False:
                        occupied_adjacent = 0
                        for adj_seat_pos in curr_seat.neighbours:
                            adj_seat = minimap[adj_seat_pos[0]][adj_seat_pos[1]]
                            if adj_seat.occupied:
                                occupied_adjacent += 1
                        if occupied_adjacent == 0:
                            changes = True
                            curr_seat.next_state_occupied = True
                        else:
                            curr_seat.next_state_occupied = False
                    else:
                        occupied_adjacent = 0
                        for adj_seat_pos in curr_seat.neighbours:
                            adj_seat = minimap[adj_seat_pos[0]][adj_seat_pos[1]]
                            if adj_seat.occupied:
                                occupied_adjacent += 1
                        if occupied_adjacent >= 5:
                            changes = True
                            curr_seat.next_state_occupied = False
                        else:
                            curr_seat.next_state_occupied = True

        for i in range(len(minimap)):
            for j in range(len(minimap[0])):
                if minimap[i][j] != None:
                    minimap[i][j].occupied = minimap[i][j].next_state_occupied

    total_occupied_seats = 0

    for i in range(len(minimap)):
        for j in range(len(minimap[0])):
            if minimap[i][j] != None and minimap[i][j].occupied == True:
                total_occupied_seats += 1



    return total_occupied_seats


print(part_2())