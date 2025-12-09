with open("input.txt", "r") as f:
    aoc = f.read()


result = 0
map_ = aoc.split()
map_ = [list(row) for row in map_]

def check_surroundings(x, y, map_):
    res = 0
    for yoff in [1, 0, -1]:
        for xoff in [1, 0, -1]:
            if x+xoff >= 0 and y+yoff >= 0 and x+xoff < len(map_[0]) and y+yoff < len(map_) and not (xoff == 0 and yoff == 0):
                if map_[y+yoff][x+xoff] == "@":
                    res += 1
    return res

have_moved = True
while have_moved:
    have_moved = False
    for y in range(len(map_)):
        for x in range(len(map_[0])):
            if map_[y][x] == "@":
                if (surroundings := check_surroundings(x, y, map_)) < 4:
                    result += 1
                    have_moved = True
                    map_[y][x] = "."

print(result)