class Ticket:
    def __init__(self, init_line):
        self.values = []
        for val in init_line.split(","):
            self.values.append(int(val))

class Field:
    def __init__(self, departure, lower, higher):
        self.departure = departure
        self.lower = lower
        self.higher = higher
        self.valid_positions = []
        self.pos = -1


def part_2():
    file = open('input.txt', 'r')
    fields = []
    tickets = []

    for line in file:
        line = line.strip('\n')
        if line == "":
            break
        field_vals = line.split(":")[1].split(" or ")
        curr_field = Field("departure" in line.split(":")[0], [int(field_vals[0].split("-")[0]),int(field_vals[0].split("-")[1])], [int(field_vals[1].split("-")[0]),int(field_vals[1].split("-")[1])])
        fields.append(curr_field)

    file.readline()
    my_ticket = Ticket(file.readline())
    tickets.append(my_ticket)
    file.readline()
    file.readline()

    invalid_sum = 0

    for line in file:
        line = line.strip('\n')
        bad_ticket = False
        current_ticket = Ticket(line)
        for val_string in line.split(","):
            val = int(val_string)
            bad_val = True
            for field in fields:
                if val >= field.lower[0] and val <= field.lower[1] or val >= field.higher[0] and val <= field.higher[1]:
                    bad_val = False
                    break
            if bad_val:
                invalid_sum += val
                bad_ticket = True
                break
        if bad_ticket == False:
            tickets.append(current_ticket)

    num_of_positions = len(fields)

    for field in fields:
        for pos in range(num_of_positions):
            valid_position_for_current_range = True
            for ticket in tickets:
                if not ((ticket.values[pos] >= field.lower[0] and ticket.values[pos] <= field.lower[1]) or (ticket.values[pos] >= field.higher[0] and ticket.values[pos] <= field.higher[1])) :
                    valid_position_for_current_range = False
                    break
            if valid_position_for_current_range:
                field.valid_positions.append(pos)

    change = True

    while change:
        change = False
        for field in fields:
            if len(field.valid_positions) == 1:
                change = True
                pos_to_remove = field.valid_positions[0]
                field.pos = pos_to_remove
                for neighbor in fields:
                    if pos_to_remove in neighbor.valid_positions:
                        neighbor.valid_positions.remove(pos_to_remove)

    answer = 1
    for field in fields:
        if field.departure:
            answer *= my_ticket.values[field.pos]

    return answer

print(part_2())