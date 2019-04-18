#!/usr/bin/env python
#20190414
import os 
import shutil
import time

### background: I notice that the mesh files and .binvox files at NYC, numbers do not match up. There are around 100,000 mesh files not converted to .binvox files. This program aims to move the meshes that have already been converted to .binvox to those that haven't.

vox_dir = "/data/city/nyc/nyc_binvox"
mesh_curr_dir = "/data/city/nyc/nyc_poly_objs"
unfinished_mesh_dir = "/data/city/nyc/nyc_mesh_undo"

"""
all_mesh = os.listdir(mesh_curr_dir)

start = time.time()
for i, f in enumerate(all_mesh):
    if (i % 1000 == 0):
        print("Now checking the {0}-th file. Elapsed time {1:.2f} min.".format(i, (time.time() - start)/60))
    suffix = f.split(".")[1]
    bid = f.split(".")[0]
    # check if corresponding binvox file exists
    binvox_name = bid + "." + "binvox"
    binvox_path = os.path.join(vox_dir, binvox_name) 
    if not os.path.exists(binvox_path):
        src_obj_path = os.path.join(mesh_curr_dir, f) # current location
        dst_obj_path = os.path.join(unfinished_mesh_dir, f)   # dest location
        shutil.move(src_obj_path, dst_obj_path)
"""

### New scenerio: After the last step, there are 120 .binvox files do not have corresponding mesh files!!! This could only be because of duplicated files. Move the files that are do not have a mesh correspondent to the other folder.

extra_vox_dir = "/data/city/nyc/nyc_binvox_extra"  # to store extra binvox files

all_vox = os.listdir(vox_dir)
start = time.time()
for i, f in enumerate(all_vox):
    if (i % 1000 == 0):
        print("Now checking the {0}-th file. Elapsed time {1:.2f} min.".format(i, (time.time() - start)/60))
    suffix = f.split(".")[1]
    bid = f.split(".")[0]
    # check if corresponding binvox file exists
    mesh_name = bid + ".obj"
    mesh_path = os.path.join(mesh_curr_dir, mesh_name) 
    if not os.path.exists(mesh_path):
        src_vox_path = os.path.join(vox_dir, f) # current location
        dst_vox_path = os.path.join(extra_vox_dir, f)   # dest location
        shutil.move(src_vox_path, dst_vox_path)

