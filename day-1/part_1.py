with open("input.txt", "r") as f:
    aoc = f.read()

result = 0
for id_rng in aoc.split(","):
    id_rng = id_rng.split("-")
    for id_ in range(int(id_rng[0]), int(id_rng[1]) + 1):
        id_ = str(id_)
        print(len(id_) // 2)
        if id_[0:len(id_) // 2] == id_[len(id_) // 2:]:
            result += int(id_)

print(result)
