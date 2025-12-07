import time
import functools
with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############

rows = aoc_input.split()
rows = [list(row) for row in rows]

rows[0][rows[0].index("S")] = "|"
for y in range(1, len(rows)):
    for x in range(0, len(rows[0])):
        if rows[y-1][x] == "|":
            if rows[y][x] == "^":
                rows[y][x-1], rows[y][x+1] = "|", "|"
                result += 1
            else:
                rows[y][x] = "|"

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")