with open("input.txt", "r") as f:
    aoc = f.read()


banks = [list(bank) for bank in aoc.split()]
result = 0

for bank in banks:
    print(bank)
    first = max(bank[:-1], key=lambda x: int(x))
    first_index = bank.index(first)
    second = max(bank[first_index+1:], key=lambda x: int(x))
    print(first, second)
    result += int(first+second)

print(result)