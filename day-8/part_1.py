import time
import functools


with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############
positions = [[int(x) for x in position.split(",")] for position in aoc_input.split("\n")]

largest_area = 0

while positions:
    position_a = positions.pop()
    for position_b in positions:
        area = (abs(position_a[0]-position_b[0])+1)*(abs(position_a[1]-position_b[1])+1)
        if area > largest_area:
            largest_area = area

result = largest_area

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")