import hashlib 

inp = "bgvyzdsv"

def part1():
    start = 0
    while True:
        test = inp + str(start)
        if hashlib.md5(str.encode(test)).hexdigest()[:5] == "00000":
            return start
        start += 1

print(part1())