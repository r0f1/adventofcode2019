with open("input.txt") as f:
    mass = [int(x) for x in f]

print(sum(x//3-2 for x in mass))

def calc(x):
    if x <= 0: return 0
    f = int(x) // 3 - 2
    if f <= 0: return 0
    return f + calc(f)

print(sum(calc(x) for x in mass))