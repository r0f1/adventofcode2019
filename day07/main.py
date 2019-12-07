from itertools import permutations

def computer(c, inputs, ptr=None):
    if ptr is None:
        ptr = [0]

    def t(pm, k, c=c):
        if pm == 0: return c[k]
        else: return k

    def get(c=c, ptr=ptr):
        r = c[ptr[0]]
        ptr[0] += 1
        return r

    while True:
        p = get()
        op = p % 100
        pm1, pm2 = (p//100)%10, (p//1000)%10

        if op in (1, 2):
            arg1, arg2, argres = get(), get(), get()
            if op == 1:
                c[argres] = t(pm1, arg1) + t(pm2, arg2)
            else:
                c[argres] = t(pm1, arg1) * t(pm2, arg2)
        elif op in (3, 4):
            arg = get()
            if op == 3:
                c[arg] = int(next(inputs))
            else:
                return t(pm1, arg), c, ptr
        elif op in (5, 6):
            arg1, arg2 = get(), get()
            if (op == 5 and t(pm1, arg1) != 0) or (op == 6 and t(pm1, arg1) == 0):
                ptr[0] = t(pm2, arg2)
        elif op in (7, 8):
            arg1, arg2, arg3 = get(), get(), get()
            if op == 7:
                c[arg3] = int(t(pm1, arg1) < t(pm2, arg2))
            else:
                c[arg3] = int(t(pm1, arg1) == t(pm2, arg2))
        else:
            break

res = []
for settings in permutations([0,1,2,3,4]):
    inp = 0
    for i in range(5):
        with open("input.txt") as f:
            c = list(map(int, f.read().strip().split(",")))
        inp = computer(c, iter([settings[i], inp]))[0]
    res.append(inp)

print(max(res))


res = []
for settings in permutations([5,6,7,8,9]):
    programs = []
    for _ in range(5):
        with open("input.txt") as f:
            programs.append(list(map(int, f.read().strip().split(","))))

    ptrs = [[0] for _ in range(5)]

    inp = 0
    first = True
    
    while True:
        for i in range(5):
            if first:
                inp, mem, ptr = computer(programs[i], iter([settings[i], inp]))
            else:
                comprun = computer(programs[i], iter([inp]), ptr=ptrs[i])
                if comprun is None:
                    break
                else:
                    inp, mem, ptr = comprun

            programs[i] = mem
            ptrs[i] = ptr
        else:
            first = False
            continue
        break

    res.append(inp)

print(max(res))
