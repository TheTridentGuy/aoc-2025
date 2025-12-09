import time
import functools


with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############

aoc_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

positions = [[int(x) for x in position.split(",")] for position in aoc_input.split("\n")]
og_positions = positions[:]
largest_area = 0

def check_collisions(position_a, position_b):
    x1, y1 = position_a
    x2, y2 = position_b
    for pos_x, pos_y in og_positions:
        if min(x1, x2) < pos_x < max(x1, x2) and min(y1, y2) < pos_y < max(y1, y2):
            return False
    return True

while positions:
    position_a = positions.pop()
    for position_b in positions:
        area = (abs(position_a[0]-position_b[0])+1)*(abs(position_a[1]-position_b[1])+1)
        if area > largest_area and check_collisions(position_a, position_b):
            largest_area = area

result = largest_area

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")