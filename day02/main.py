from itertools import product
from more_itertools import chunked

with open("input.txt") as f:
    codes = list(map(int, f.read().strip().split(",")))

codes[1] = 12
codes[2] = 2

for c, pos1, pos2, posres in chunked(codes, 4):
    if c == 1:
        codes[posres] = codes[pos1] + codes[pos2]
    elif c == 2:
        codes[posres] = codes[pos1] * codes[pos2]
    else:
        break

print(codes[0])


for a, b in product(range(100), range(100)):

    with open("input.txt") as f:
        codes = list(map(int, f.read().strip().split(",")))

    codes[1] = a
    codes[2] = b

    for c, pos1, pos2, posres in chunked(codes, 4):
        if c == 1:
            codes[posres] = codes[pos1] + codes[pos2]
        elif c == 2:
            codes[posres] = codes[pos1] * codes[pos2]
        else:
            break

    if codes[0] == 19690720:
        print(100*a+b)