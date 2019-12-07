def get_chain(b):
    res = []
    try:
        while True:
            b = d[b]
            res.append(b)
    except KeyError:
        pass
    return res

with open("input.txt") as f:
    data = [x.strip().split(")") for x in f]

d = {b: a for a, b in data}

count = 0
for a, b in d.items():
  count += 1+len(get_chain(b))
print(count)

you = get_chain("YOU")
san = get_chain("SAN")

count = 0
yp, sp = len(you)-1, len(san)-1
while you[yp] == san[sp]:
    yp, sp = yp-1, sp-1
    count += 1
    
print((len(you)-count) + (len(san)-count))
