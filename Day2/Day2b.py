import re


def is_invalid(n):
    s = str(n)
    length = len(s)
    return any(
        length % i == 0 and s == s[:i] * (length // i)
        for i in range(1, length // 2 + 1)
    )

res = []
with open("Day2/Day2.txt", "r") as file:
    ranges = file.read().strip().split(",")

parsed_ranges = []
for r in ranges:
    start, end = map(int, r.split("-"))
    parsed_ranges.append((start, end))

invalid_ids = 0
for start, end in parsed_ranges:
    for n in range(start, end + 1):
        if is_invalid(n):
            invalid_ids += n

print(invalid_ids)