import time
import functools
with open("input.txt", "r") as f:
    aoc_input = f.read()
result = 0
aoc_time_start = time.perf_counter()
##############
# CODE BELOW #
##############
import math



boxes = aoc_input.split()
boxes = [[int(x) for x in box.split(",")] for box in boxes]

def euclidean_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)

distances = []
og_boxes = boxes[:]
while boxes:
    box_a = boxes.pop()
    for box_b in boxes:
        distances.append((box_a, box_b, euclidean_distance(*box_a, *box_b)))

distances.sort(key=lambda x: x[-1])

circuits = []
for _ in range(1000):
    next_closest = distances.pop(0)
    box_a, box_b, _ = next_closest
    circuit_a = None
    circuit_b = None
    for i in range(len(circuits)):
        if box_a in circuits[i]:
            circuit_a = i
        if box_b in circuits[i]:
            circuit_b = i
    if circuit_a and circuit_b and circuit_a == circuit_b:
        pass
    elif circuit_a and circuit_b and not circuit_a == circuit_b:
        new_circuit = [*circuits[circuit_a], *circuits[circuit_b]]
        circuits = [circuits[i] for i in range(len(circuits)) if not i in (circuit_a, circuit_b)]
        circuits.append(new_circuit)
    elif circuit_a:
        circuits[circuit_a].append(box_b)
    elif circuit_b:
        circuits[circuit_b].append(box_a)
    else:
        circuits.append([box_a, box_b])

circuits.sort(key=lambda x: len(x))
result = len(circuits[-3])*len(circuits[-2])*len(circuits[-1])

##############
# CODE ABOVE #
##############
print()
print(result)
print(f"execution time: {(time.perf_counter()-aoc_time_start)*1000:.2f}ms")