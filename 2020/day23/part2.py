class Cup():
    def __init__(self, id):
        self.id = id
        self.next = None


def part_2():
    cups = {}

    nums = [int(num) for num in open('input.txt').read()]

    for num in nums:
        new_cup = Cup(num)
        cups[num] = new_cup

    for num in range(10, 1000001):
        new_cup = Cup(num)
        cups[num] = new_cup

    for i in range(len(nums) - 1):
        cups[nums[i]].next = cups[nums[i + 1]]
    cups[nums[len(nums) - 1]].next = cups[10]
    for i in range(10, 1000000):
        cups[i].next = cups[i + 1]
    cups[1000000].next = cups[nums[0]]


    current_cup = cups[nums[0]]
    move = 0
    while move < 10000000:
        removed_ids = [current_cup.next.id, current_cup.next.next.id, current_cup.next.next.next.id]
        current_cup.next = current_cup.next.next.next.next
        destination_cup_id = current_cup.id - 1
        if destination_cup_id == 0:
            destination_cup_id = 1000000
        while destination_cup_id in removed_ids:
            destination_cup_id -= 1
            if destination_cup_id == 0:
                destination_cup_id = 1000000

        destination_cup = cups[destination_cup_id]
        cups[removed_ids[2]].next = destination_cup.next
        destination_cup.next = cups[removed_ids[0]]
        current_cup = current_cup.next
        move += 1



    star_1 = cups[1].next.id
    star_2 = cups[1].next.next.id

    return star_1 * star_2


print(part_2())