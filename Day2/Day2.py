import re

res = []
with open("Day2/Day2.txt", "r") as file:
    ranges = file.read().strip().split(",")

parsed_ranges = []
for r in ranges:
    start, end = map(int, r.split("-"))
    parsed_ranges.append((start, end))

def is_invalid(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

invalid_ids = 0
for start, end in parsed_ranges:
    for n in range(start, end + 1):
        if is_invalid(n):
            invalid_ids += n

print(invalid_ids)
