import itertools
import re
import time
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
    button_combos = [[[False]*len(indicator_lights), (wiring,)] for wiring in button_wirings]
    for combinations in [itertools.combinations(button_wirings, i) for i in range(2, len(indicator_lights))]:
        for combination in combinations:
            button_combos.append([[False]*len(indicator_lights), combination])
    target = [True if light == "#" else False for light in indicator_lights]
    presses = 0
    for i in range(100000):
        for combo in button_combos:
            lights, buttons = combo
            for button in buttons:
                for light in button:
                    lights[light] = not indicator_lights[light]
            if lights == target:
                return presses*len(combo)
    else:
        print("warning loop exited", machine)
        return 0


for machine in machines:
    result += solve_machine(machine)
    print("solved machine")


##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")