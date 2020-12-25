
def get_loop_size_for(subject_num, pub_key):
    value = 1
    loop_times = 0
    while value != pub_key:
        loop_times += 1
        value *= subject_num
        value = value % 20201227
    
    return loop_times

def part_1():
    card_pub, door_pub = [int(num) for num in open('input.txt').read().split("\n")]

    card_loop_size = get_loop_size_for(7, card_pub)

    answer = 1

    for _ in range(card_loop_size):
        answer *= door_pub
        answer = answer % 20201227

    return answer

print(part_1())