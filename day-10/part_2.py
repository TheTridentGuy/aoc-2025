import re
import time

with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############

from machine_solver import solve_machine

machines = aoc_input.split("\n")
for machine in machines:
    button_wirings = [tuple(map(int, wiring.split(","))) for wiring in re.findall(r"(?<=\()\S+(?=\))", machine)]
    joltages = tuple([int(joltage) for joltage in re.findall(r"(?<=\{)\S+(?=})", machine)[0].split(",")])
    result += solve_machine(joltages, button_wirings)

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")