from collections import Counter
from more_itertools import pairwise

def cond1(n):
    for a, b in pairwise(str(n)):
        if int(a) > int(b):
            return False
    return True

def cond2(n):
    for a, b in pairwise(str(n)):
        if a == b:
            return True
    return False

def cond3(n):
    c = set(Counter(str(n)).values())
    return len(c & {2}) > 0

nrs = [i for i in range(372304, 847060) if cond1(i) and cond2(i)]
print(len(nrs))

nrs2 = [i for i in nrs if cond3(i)]
print(len(nrs2))
