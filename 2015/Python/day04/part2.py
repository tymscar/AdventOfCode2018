import hashlib 

inp = "bgvyzdsv"

def part2():
    start = 0
    while True:
        test = inp + str(start)
        if hashlib.md5(str.encode(test)).hexdigest()[:6] == "000000":
            return start
        start += 1

print(part2())