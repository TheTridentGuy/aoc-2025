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
carpet_size = 100000
carpet = [[False]*carpet_size for _ in range(carpet_size)]

last_x, last_y = None, None
for x, y in [*positions, positions[0]]:
    if last_x and last_y:
        if last_x < x:
            for new_x in range(last_x+1, x):
                carpet[y][new_x] = True
        elif x < last_x:
            for new_x in range(last_x-1, x, -1):
                carpet[y][new_x] = True
        elif last_y < y:
            for new_y in range(last_y+1, y):
                carpet[new_y][x] = True
        elif y < last_y:
            for new_y in range(last_y-1, y, -1):
                carpet[new_y][x] = True
    carpet[y][x] = True
    last_x, last_y = x, y

def flooodfill(x, y):
    if not carpet[y][x]:
        carpet[y][x] = True
        for x_off, y_off in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            flooodfill(x+x_off, y+y_off)

y = 69
for x in range(carpet_size):
    if carpet[y][x]:
        flooodfill(x+1, y)
        break

largest_area = 0

def perimeter_walk(position_a, position_b):
    (x1, y1), (x2, y2) = position_a, position_b
    corners = [(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)]
    last_x, last_y = None, None
    for x, y in corners:
        if not carpet[y][x]: return False
        if last_x and last_y:
            if last_x < x:
                for new_x in range(last_x+1, x):
                    if not carpet[y][new_x]: return False
            elif x < last_x:
                for new_x in range(last_x-1, x, -1):
                    if not carpet[y][new_x]: return False
            elif last_y < y:
                for new_y in range(last_y+1, y):
                    if not carpet[new_y][x]: return False
            elif y < last_y:
                for new_y in range(last_y-1, y, -1):
                    if not carpet[new_y][x]: return False
        last_x, last_y = x, y
    return True

while positions:
    position_a = positions.pop()
    for position_b in positions:
        area = (abs(position_a[0]-position_b[0])+1)*(abs(position_a[1]-position_b[1])+1)
        if area > largest_area and perimeter_walk(position_a, position_b):
            print(area, position_a, position_b)
            largest_area = area

result = largest_area

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")
