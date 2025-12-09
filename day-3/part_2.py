from string import digits

with open("input.txt", "r") as f:
    aoc = f.read()


banks = [list(bank) for bank in aoc.split()]
result = 0
joltages = []


def get_joltage(bank, digits):
    bank = [int(digit) for digit in bank]
    start = 0
    end = -(digits-1)
    for i in range(digits):
        range_ = bank[start:end] if end < 0 else bank[start:]
        digit = max(range_)
        print(start, end, range_, f"-> {digit}")
        yield str(digit)
        start += range_.index(digit) + 1
        end += 1

for bank in banks:
    print(bank)
    joltage = int("".join(get_joltage(bank, 12)))
    print(joltage)
    joltages.append(joltage)

print(sum(joltages))