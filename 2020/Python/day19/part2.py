import re

def get_regex_string(rule, depth, max_depth, rules):
    if depth > max_depth: # Don't go on forever
        return ''

    if rules[rule][0] == '"': # This only happens when the rule points to "a" or "b"
        return rules[rule][1]

    current_rules = []
    for inner_rule_set in rules[rule].split('|'):
        inner_answer = []
        for inner_rule in inner_rule_set.split():
            inner_answer.append(get_regex_string(inner_rule, depth + 1, max_depth, rules))
        current_rules.append("".join(inner_answer))

    return '(' + '|'.join(current_rules) + ')'

def part_2():
    rules_string, tests = open('input.txt').read().split('\n\n')
    rules = {}
    for line in rules_string.split("\n"):
        rules[line.split(": ")[0]] = line.split(": ")[1]

    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"

    regex = re.compile(get_regex_string('0', 0, 14, rules))

    count = 0

    for test in tests.split():
        if regex.fullmatch(test):
            count += 1

    return count

print(part_2())