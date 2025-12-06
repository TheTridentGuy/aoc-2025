import time
with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############
import sys
rows = aoc_input.split("\n")
rows = [list(row) for row in rows]
rows[-1].extend([" ", " "]) # pov: your editor strips trailing spaces from your input file

numbers = []
for x in range(len(rows[0])-1, -1, -1):
    number = []
    for y in range(len(rows)):
        if rows[y][x] == " ":
            continue
        elif rows[y][x] in "*+":
            numbers.append("".join(number))
            numbers = [number for number in numbers if number]
            solution = None
            exec(f"solution={rows[y][x].join(numbers)}")
            result += solution
            number = []
            numbers = []
        else:
            number.append(rows[y][x])
    numbers.append("".join(number))


##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")