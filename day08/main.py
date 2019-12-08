import numpy as np
from pprint import pprint

with open("input.txt") as f:
    img = np.array([int(i) for i in [x.strip() for x in f][0]])
    img = img.reshape((100,6,25))

counts = np.count_nonzero(img, axis=(1,2))
s = img[np.argmax(counts),:,:]
print(np.sum(s == 1)*np.sum(s == 2))

mask = (img == 2).astype(np.int)
choose = np.argmin(mask, axis=0)

res = []
for row_idx, row in enumerate(choose):
    r = []
    for col_idx, l in enumerate(row):
        r.append(img[l, row_idx, col_idx])
    res.append(r)

pprint(res)
