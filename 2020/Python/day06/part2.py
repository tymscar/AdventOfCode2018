def part_2():
    file = open('input.txt', 'r')

    count = 0
    answered_questions = {}
    people_answering = 0

    for lineWithOptionNewLine in file:
        if lineWithOptionNewLine == "\n":
            for char in answered_questions:
                if answered_questions[char] == people_answering:
                    count += 1
            answered_questions = {}
            people_answering = 0
        else:
            people_answering += 1
            line = lineWithOptionNewLine.strip('\n')
            for char in line:
                if char in answered_questions:
                    answered_questions[char] += 1
                else:
                    answered_questions[char] = 1
    for char in answered_questions:
        if answered_questions[char] == people_answering:
            count += 1

    return count


print(part_2())
