import itertools
import re
import time

from fontTools.misc.cython import returns

with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############

machines = aoc_input.split("\n")
for index, machine in enumerate(machines):
    indicator_lights = list(re.findall(r"(?<=\[).+(?=])", machine)[0])
    button_wirings = [tuple(map(int, wiring.split(","))) for wiring in re.findall(r"(?<=\()\S+(?=\))", machine)]
    machines[index] = (indicator_lights, button_wirings)

def solve_machine(machine):
    indicator_lights, button_wirings = machine
    button_combos = []
    for combinations in [itertools.combinations(button_wirings, i) for i in range(1, len(button_wirings))]:
        for combination in combinations:
            button_combos.append(combination)
    target = [True if light == "#" else False for light in indicator_lights]
    shortest = float("inf")
    for combo in button_combos:
        lights = [False]*len(indicator_lights)
        for button in combo:
            for light in button:
                lights[light] = not lights[light]
        if lights == target and len(combo) < shortest:
            shortest = len(combo)
    return shortest



for machine in machines:
    result += solve_machine(machine)
    print("solved machine")


##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")