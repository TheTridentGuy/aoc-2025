import time
from functools import lru_cache

with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############

routings = [routing.split(":") for routing in aoc_input.split("\n")]

with open("graph.dot", "w") as f:
    f.writelines(["digraph {\n"])
    for routing in routings:
        f.writelines([f"{routing[0]} -> {{{routing[1]}}}\n"])
    f.writelines(["}"])
graph = {}
for routing in routings:
    graph[routing[0]] = routing[1].split()

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")