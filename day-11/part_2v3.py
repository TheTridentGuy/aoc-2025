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
def find_paths_to(node, target):
    connected_nodes = graph.get(node)
    if not connected_nodes:
        return 0
    elif target in connected_nodes:
        return 1
    else:
        return sum([find_paths_to(connected_node, target) for connected_node in graph[node]])


result = max(find_paths_to("svr", "fft") * find_paths_to("fft", "dac") * find_paths_to("dac", "out"),
             find_paths_to("svr", "dac") * find_paths_to("dac", "fft") * find_paths_to("fft", "out"))

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")