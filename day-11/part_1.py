import time
from os.path import split

with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############

routings = [routing.split(":") for routing in aoc_input.split("\n")]
graph = {}
for routing in routings:
    graph[routing[0]] = routing[1].split()

def find_paths_to_out(nodes):
    if "out" in nodes:
        return 1
    else:
        return sum([find_paths_to_out(graph[node]) for node in nodes])

result = find_paths_to_out(["you"])

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")