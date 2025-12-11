DIGIT_COUNT = 12

def find_highest_joltage(batteries, digit_count):
    if not batteries:
        return None

    if len(batteries) < digit_count:
        return None
    
    start, chosen = 0, []

    while digit_count > 0:
        max_digit = max_index = -1
        end = len(batteries) - digit_count
        for i in range(start, end + 1):
            if batteries[i] > max_digit:
                max_digit = batteries[i]
                max_index = i
        
        chosen.append(max_digit)
        start = max_index + 1
        digit_count -= 1
    
    joltage = int("".join(str(j) for j in chosen))
    return joltage
    
res = 0
with open("Day3/Day3.txt", "r") as file:
    for bank in file:
        batteries = [int(b) for b in bank.strip()]
        highest_joltage = find_highest_joltage(batteries, DIGIT_COUNT)
        if highest_joltage:
            print(highest_joltage)
            res += highest_joltage

    print(res)