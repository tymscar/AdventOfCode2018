def part_1():
    file = open('input.txt', 'r')

    count = 0
    answered_questions = {}

    for lineWithOptionNewLine in file:
        if lineWithOptionNewLine == "\n":
            count += len(answered_questions)
            answered_questions = {}
        else:
            line = lineWithOptionNewLine.strip('\n')
            for char in line:
                answered_questions[char] = True
    count += len(answered_questions)

    return count


print(part_1())