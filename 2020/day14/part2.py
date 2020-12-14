def get_addresses(mask, location):
    main_address = []
    location_string = (38-len(bin(location))) * "0" + bin(location)[2:]

    for i in range(len(mask)):
        if mask[i] == "0":
            main_address.append(location_string[i])
        else:
            main_address.append(mask[i])

    addresses = []
    stringed_addresses = get_addresses_string("".join(main_address))
    for address in stringed_addresses:
        addresses.append(int(address,2))

    return addresses

def get_addresses_string(from_main_address):
    addresses = []

    for i in range(len(from_main_address)):
        if from_main_address[i] == "X":
            addresses += get_addresses_string(from_main_address[:i] + "1" + from_main_address[i+1:])
            addresses += get_addresses_string(from_main_address[:i] + "0" + from_main_address[i + 1:])
            return addresses

    return [from_main_address]

def part_2():
    file = open('input.txt', 'r')
    memory = {}

    for line in file:
        line = line.strip("\n").split(" = ")
        if line[0] == "mask":
            mask = line[1]
        else:
            location = int(line[0].split("[")[1].strip("]"))
            value = int(line[1])
            addresses = get_addresses(mask, location)
            for add in addresses:
                memory[add] = value

    total_in_memory = 0

    for val in memory.values():
        total_in_memory += val

    return total_in_memory

print(part_2())