with open("input.txt", "r") as f:
    aoc = f.read()


result = 0
with open("input.txt", "r") as f:
    aoc = f.read()


result = 0

ranges, ids = aoc.split("\n\n")
ranges = ranges.split()
ids = ids.split()
ids = [int(id) for id in ids]

challenge = []

for start_end in ranges:
    start_end = start_end.split("-")
    challenge.append(f"{start_end[0]} <= num <= {start_end[1]}")

challenge = " or ".join(challenge)

for id in ids:
    x = False
    exec("x = "+ challenge.replace("num", str(id)))
    if x:
        result += 1
print(result)