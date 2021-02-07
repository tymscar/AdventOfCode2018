from functools import reduce

def calculate(expression, start, end):
    current = start
    answer = []
    current_ans = 0

    while current < end:

        if expression[current] == "*":
            answer.append(current_ans)
            current_ans = 0
        elif expression[current] == "(":
            parentheses_value = 1
            parentheses_end = current + 1
            while parentheses_value > 0:
                if expression[parentheses_end] == ")":
                    parentheses_value -= 1
                elif expression[parentheses_end] == "(":
                    parentheses_value += 1
                parentheses_end += 1
            parentheses_end -= 1

            current_ans += calculate(expression, current+1,parentheses_end)
            current = parentheses_end

        elif expression[current] != " " and expression[current] != "+":
            current_ans += int(expression[current])

        current += 1
    answer.append(current_ans)

    return reduce((lambda x, y: x * y), answer)

def part_2():
    file = open('input.txt', 'r')
    sum = 0

    for line in file:
        line = line.strip('\n')
        sum += calculate(line, 0, len(line))

    return sum


print(part_2())