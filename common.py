#!/usr/bin/env python
### a program to compare how many files in two directories are the same
import os

# d1 = "/data/city/zurich/zurich_new_objs"
# d2 = "/data/city/zurich/zurich_new_objs_2"
d1 = "pcd.txt"
d2 = "vox64.txt"

# f1 = os.listdir(d1)
# f2 = os.listdir(d2)

with open(d1, 'r') as f:
    pcd = f.readlines()

with open(d2, 'r') as f:
    vox = f.readlines()

print("pcd: {0}".format(len(pcd)))
print("vox: {0}".format(len(vox)))

pcd = [x.strip() for x in pcd]
vox = [x.strip() for x in vox]

# common = set(f1) & set(f2)
# print("Common : {0}".format(len(common)))
num = 100000
res = []
for i in range(num):
    tmp = pcd[i].split(".")[0]   # building ID only
    if tmp + ".bin" in vox:
        print("Found!")
        res.append(tmp)
    else:
        continue

def list2file(l, path):
    """
    output a list to file.
    """
    with open(path, 'a+') as f:
        for item in l:
            f.write("%s\n" % item)
    return


list2file(res, "common100000.txt")
