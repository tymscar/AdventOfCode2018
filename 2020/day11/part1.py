class Seat():
    def __init__(self):
        self.occupied = False
        self.next_state_occupied = False
        self.neighbours = []


def get_neighbours(minimap, posy, posx):
    neighbours = []
    possible = [(posy - 1, posx - 1), (posy - 1, posx), (posy - 1, posx + 1), (posy, posx + 1), (posy + 1, posx + 1), (posy + 1, posx), (posy + 1, posx - 1), (posy, posx - 1)]
    for possible_neighbour in possible:
        if possible_neighbour[0] >= 0 and possible_neighbour[0] < len(minimap) and possible_neighbour[1] >= 0 and possible_neighbour[1] < len(minimap[0]) and minimap[possible_neighbour[0]][possible_neighbour[1]] != None:
            neighbours.append(possible_neighbour)
    
    return neighbours

def part_1():
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
                        if occupied_adjacent >= 4:
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


print(part_1())