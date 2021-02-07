def minutes_to_earliest_arrival(of_bus, to_date):
    return of_bus - (to_date % of_bus)

def part_1():
    file = open('input.txt', 'r')

    departure_time = int(file.readline())
    timetable = [int(bus) for bus in file.readline().split(sep=",") if bus != "x"]

    earliest_bus = timetable[0]
    earliest_bus_time = minutes_to_earliest_arrival(earliest_bus, departure_time)

    for bus in timetable:
        if minutes_to_earliest_arrival(bus, departure_time) < earliest_bus_time:
            earliest_bus = bus
            earliest_bus_time = minutes_to_earliest_arrival(bus, departure_time)

    return earliest_bus * earliest_bus_time

print(part_1())
