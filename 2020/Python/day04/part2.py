class Document:
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
        self.cm = True

    def is_valid_passport(self):
        return self.byr is not None and self.iyr is not None and self.eyr is not None and self.hgt is not None and self.hcl is not None and self.ecl is not None and self.pid is not None

    def assign(self, metric, value):
        value = ' '.join(value.split())
        if metric == "byr":
            if value.isnumeric() and 1920 <= int(value) <= 2002:
                self.byr = value
        elif metric == "iyr":
            if value.isnumeric() and 2010 <= int(value) <= 2020:
                self.iyr = value
        elif metric == "eyr":
            if value.isnumeric() and 2020 <= int(value) <= 2030:
                self.eyr = value
        elif metric == "hgt":
            if value[-2:] == "cm":
                height = value[:-2]
                if height.isnumeric() and 150 <= int(height) <= 193:
                    self.hgt = height
                    self.cm = True
            if value[-2:] == "in":
                height = value[:-2]
                if height.isnumeric() and 59 <= int(height) <= 76:
                    self.hgt = height
                    self.cm = False
        elif metric == "hcl":
            if value[0] == "#" and len(value) == 7:
                invalid_chars = 0
                chars_to_use = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                for letter in value[1:]:
                    if letter not in chars_to_use:
                        invalid_chars += 1
                if invalid_chars == 0:
                    self.hcl = value
        elif metric == "ecl":
            valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if value in valid_ecl:
                self.ecl = value
        elif metric == "pid":
            if value.isnumeric() and len(value) == 9:
                self.pid = value
        elif metric == "cid":
            self.cid = value


def part_2():
    file = open('input.txt', 'r')
    valid_passports = 0

    curr = Document()
    for line in file:
        if line == "\n":
            if curr.is_valid_passport():
                valid_passports += 1
            curr = Document()
        else:
            for metric in line.split(" "):
                curr.assign(metric[:3], metric[4:])
    if curr.is_valid_passport():
        valid_passports += 1

    return valid_passports


print(part_2())
