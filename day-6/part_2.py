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

def recursive(x, y):
    try:
        while rows[y][x] == ".":
            y+=1
        assert rows[y][x] == "^"
        return recursive(x-1, y+1)+recursive(x+1, y+1)
    except IndexError:
        return 1


for x in range(len(rows[0])):
    if rows[0][x] == "S":
        result += recursive(x, 1)



##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")