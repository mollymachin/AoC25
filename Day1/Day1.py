def main():
    res = 0
    with open("Day1/Day1.txt", "r") as file:
        cur = 50
        for line in file:
            line = line.strip()
            d, val = line[0], int(line[1:])

            if d == "R":
                cur += val
                if cur >= 100:   
                    rotations = cur // 100
                    res += rotations
            else:
                prev = cur
                cur -= val
                if cur <= 0:
                    rotations = 1 + (cur // -100)
                    if prev == 0:
                        rotations -= 1
                    res += rotations
            cur %= 100   
    return res

print(main())
