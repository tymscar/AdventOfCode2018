def calculate(expression, start, end):
    current = start
    answer = 0
    add = True

    while current < end:

        if expression[current] == "+":
            add = True
        elif expression[current] == "*":
            add = False
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
            if add:
                answer += calculate(expression, current+1,parentheses_end)
            else:
                answer *= calculate(expression, current + 1, parentheses_end)
            current = parentheses_end
        elif expression[current] != " ":
            if add:
                answer += int(expression[current])
            else:
                answer *= int(expression[current])
        current += 1

    return answer

def part_1():
    file = open('input.txt', 'r')
    sum = 0

    for line in file:
        line = line.strip('\n')
        sum += calculate(line, 0, len(line))

    return sum


print(part_1())