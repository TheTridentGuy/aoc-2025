import time
with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############

rows = aoc_input.split("\n")
rows = [row.split() for row in rows]

for i in range(len(rows[0])):
    x = None
    expr = f"{rows[-1][i]}".join([row[i] for row in rows[:-1]])
    expr = "x=" +expr
    exec(expr)
    result += x

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")