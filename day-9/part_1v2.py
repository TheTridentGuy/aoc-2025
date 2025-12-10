import time
import functools
from itertools import combinations

with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############

positions = [[int(x) for x in position.split(",")] for position in aoc_input.split("\n")]
result = max((abs(x1-x2)+1)*(abs(y1-y2)+1) for ((x1, y1), (x2, y2)) in combinations(positions, 2))

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")