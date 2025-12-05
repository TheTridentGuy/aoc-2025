with open("input.txt", "r") as f:
    aoc = f.read()


result = 0
with open("input.txt", "r") as f:
    aoc = f.read()



result = 0




ranges = aoc.split("\n\n")[0].split()


challenge = []

annotated = []
for index, start_end in enumerate(ranges):
    start_end = start_end.split("-")
    annotated.append(f"s{start_end[0]}-{index}")
    annotated.append(f"e{start_end[1]}-{index}")

started = False
start = 0
end = None
ends_to_be_made = []
annotated.sort(key=lambda x: int(x.split("-")[0][1:]))
print(annotated)
for arange in annotated:
    arange, index = arange.split("-")
    if not started and arange.startswith("s"):
        started = True
        ends_to_be_made.append(index)
        start = int(arange[1:])
        if end and start == end:
            result -= 1
    elif started and arange.startswith("s"):
        ends_to_be_made.append(index)
    elif arange.startswith("e"):
        ends_to_be_made.remove(index)
    if started and len(ends_to_be_made) == 0:
        started = False
        end = int(arange[1:])
        print(start, end, (end-start) + 1)
        result += (end-start) + 1

print()
print(result)
