import time
import functools
with open("input2.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############


rows = aoc_input.split()
rows = [list(row) for row in rows]

rows[0][rows[0].index("S")] = 0
for y in range(1, len(rows)):
    for x in range(0, len(rows[0])):
        if rows[y-1][x] == 0:
            if rows[y][x] == "^":
                rows[y][x-1], rows[y][x+1] = 0, 0
            else:
                rows[y][x] = 0

rows[0][rows[0].index(0)] = 1

for y in range(1, len(rows)):
    for x in range(0, len(rows[0])):
        if isinstance(rows[y][x], int):
            if isinstance(rows[y-1][x], int):
                rows[y][x] = rows[y-1][x]
            if x-1 >= 0 and isinstance(rows[y-1][x-1], int) and rows[y][x-1] == "^":
                rows[y][x] += rows[y-1][x-1]
            if x+1 < len(rows[0]) and isinstance(rows[y-1][x+1], int) and rows[y][x+1] == "^":
                rows[y][x] += rows[y-1][x+1]

result = sum([item for item in rows[-1] if isinstance(item, int)])

for row in rows:
    print([str(item) for item in row])

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")