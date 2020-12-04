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

    def is_valid_passport(self):
        return self.byr is not None and self.iyr is not None and self.eyr is not None and self.hgt is not None and self.hcl is not None and self.ecl is not None and self.pid is not None

    def assign(self, metric, value):
        if metric == "byr":
            self.byr = value
        elif metric == "iyr":
            self.iyr = value
        elif metric == "eyr":
            self.eyr = value
        elif metric == "hgt":
            self.hgt = value
        elif metric == "hcl":
            self.hcl = value
        elif metric == "ecl":
            self.ecl = value
        elif metric == "pid":
            self.pid = value
        elif metric == "cid":
            self.cid = value


def part_1():
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


print(part_1())
