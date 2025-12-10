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
lines = list(zip([*positions, positions[0]], [positions[-1], *positions]))
largest_area = 0

def check_collisions(position_a, position_b):
    x1, y1 = position_a
    x2, y2 = position_b
    for line in lines:
        line_x1, line_y1 = line[0]
        line_x2, line_y2 = line[1]
        if line_y1 == line_y2:
            if not min(y1, y2) < line_y1 < max(y1, y2):
                continue
            for x in range(min(line_x1, line_x2), max(line_x1, line_x2)+1):
                if min(x1, x2) < x < max(x1, x2):
                    return False
        elif line_x1 == line_x2:
            if not min(x1, x2) < line_x1 < max(x1, x2):
                continue
            for y in range(min(line_y1, line_y2), max(line_y1, line_y2)+1):
                if min(y1, y2) < y < max(y1, y2):
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