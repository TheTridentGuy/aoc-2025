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
graph = {}
for routing in routings:
    graph[routing[0]] = routing[1].split()


@lru_cache
def find_paths_to_out(node, dac=False, fft=False, visited=()):
    visited = set(visited)
    visited.add(node)
    if node == "dac":
        dac = True
    if node == "fft":
        fft = True
    if "out" in graph[node]:
        return 1 if dac and fft else 0
    else:
        return sum([find_paths_to_out(connected_node, dac, fft, tuple(visited)) for connected_node in graph[node] if not connected_node in visited])

result = find_paths_to_out("svr")

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")