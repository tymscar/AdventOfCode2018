rules = {}
memo = {}


def get_strings_from_rule(curr_rule):
    global rules
    global memo


    this_string_list = []
    
    if curr_rule in memo:
        return memo[curr_rule]

    for rule_list in rules[curr_rule]:

        strings= get_strings_from_rule(rule_list[0])
        for i in range(1,len(rule_list)):
            curr_strings = []
            for string_one in strings:
                for string_two in get_strings_from_rule(rule_list[i]):
                    curr_strings.append(string_one + string_two)
            strings = curr_strings
        this_string_list += strings


    answer = []


    for str in this_string_list:
        answer.append("".join(str))

    memo[curr_rule] = answer
    return answer

def part_1():
    global rules
    global memo
    
    file = open('input.txt', 'r')
    making_rules = True
    answer = 0

    for line in file:
        line = line.strip('\n')
        if len(line) == 0:
            making_rules = False
            rule_zero = get_strings_from_rule("0")
            len_to_match = len(rule_zero[0])
            continue
        if making_rules:
            name = line.split(": ")[0]
            rules_info = line.split(": ")[1]
            if rules_info[0] == '"':
                memo[name] = [rules_info[1]]
            else:
                curr_rules = []
                for rule in rules_info.split(" | "):
                    curr_rules.append(rule.split(" "))
                rules[name] = curr_rules
        else:
            if len(line) == len_to_match:
                if line in rule_zero:
                    answer+=1
            
            
            
    return answer


print(part_1())