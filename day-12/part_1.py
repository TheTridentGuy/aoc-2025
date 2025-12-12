import math
import time
with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############

aoc_input = aoc_input.split("\n\n")
presents = aoc_input[:-1]
presents = [present.count("#") for present in presents]
spaces = aoc_input[-1].split("\n")
spaces = [space.split(":") for space in spaces]

for size, counts in spaces:
    size = math.prod(map(int, size.split("x")))
    counts = map(int, counts.split())
    space_needed = 0
    for index, count in enumerate(counts):
        space_needed += presents[index]*count
    if space_needed <= size:
        result += 1

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")