#!/usr/bin/env python
### The situation is we did mesh to binvox on NYC data but the program crashed halfway
### So some meshes are done while others undone
### There needs a way to filter finished meshes from unfinished meshes
### We decide that instead of moving things elsewhere, we'll just write the meshes that are not yet done to a txt file

import os

def list2file(l, path):
    """
    output a list to file.
    """
    with open(path, 'a+') as f:
        for item in l:
            f.write("%s\n" % item)
    return

parent_dir = "/data/city/nyc/nyc_poly_objs"
all_files = os.listdir(parent_dir)
all_objs = [x for x in all_files if x[-4:] == ".obj"]
all_binvox = [x for x in all_files if x[-4:] != ".obj"]
unfinished_objs = [x for x in all_objs if x.split(".")[0]+".binvox" not in all_binvox]

save_dir = "/data/city/nyc/"
list2file(unfinished_objs, os.path.join(save_dir, "undone_objs.txt"))
