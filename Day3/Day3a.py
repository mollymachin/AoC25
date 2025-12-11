res = 0

with open("Day3/Day3.txt", "r") as file:
    for bank in file:
        batteries = [int(b) for b in bank.strip()]
        l, r, maxR = 0, 1, 0
        while r < len(batteries):
            if batteries[r] > batteries[l] and r < len(batteries)-1:
                l = r
                maxR = 0
            
            else:
                maxR = max(maxR, batteries[r])
            r += 1
        res += int(str(batteries[l]) + str(maxR))
    print(res)
