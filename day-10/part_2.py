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
    button_wirings = [tuple(map(int, wiring.split(","))) for wiring in re.findall(r"(?<=\()\S+(?=\))", machine)]
    joltages = tuple([int(joltage) for joltage in re.findall(r"(?<=\{)\S+(?=})", machine)[0].split(",")])
    machines[index] = (joltages, button_wirings)

def solve_machine(machine):
    pass

for machine in machines:
    result += solve_machine(machine)


##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")