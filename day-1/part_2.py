with open("input.txt", "r") as f:
    aoc = f.read()

result = 0

def repeat_chk(string):
    for i in range(len(string)//2+1):
        if string[i:] == string[:-i] and len(string)%i==0:
            print(string, string[i:], string[:-i], i)
            return True
    return False

for id_rng in aoc.split(","):
    id_rng = id_rng.split("-")
    for id_ in range(int(id_rng[0]), int(id_rng[1]) + 1):
        id_ = str(id_)
        if id_[0:len(id_) // 2] == id_[len(id_) // 2:]:
            result += int(id_)
        elif repeat_chk(id_):
            result += int(id_)
print()
print(result)
