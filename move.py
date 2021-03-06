#!/usr/bin/env python
import os 
import shutil
import time
### Purpose of this program is the binvox program crashed as server crashed
### so some meshes are finished and others unfinished 
### so we need to move all .binvox files to the other folder 

# parent_dir = "/data/gmldata/nyc_objs/"
def list2file(l, name):
    """
    output a list to file.
    """
    with open(name+".txt", 'a+') as f:
        for item in l:
            f.write("%s\n" % item)
    return

parent_dir = "/data/gmldata/nyc_objs_organized_1"
mesh_dest_dir = "/data/gmldata/nyc_finished_mesh"
vox_dest_dir = "/data/gmldata/nyc_finished_binvox"

all_files = os.listdir(parent_dir)
start = time.time()
for i, f in enumerate(all_files):
    if (i % 1000 == 0):
        print("Now checking the {0}-th file. Elapsed time {1:.2f} min.".format(i, (time.time() - start)/60))
    suffix = f.split(".")[1]
    bid = f.split(".")[0]
    if suffix == "binvox":
        try:
            binvox_name = bid + "." + "binvox"
            obj_name = bid + "." + "obj" 
            binvox_path = os.path.join(parent_dir, binvox_name) 
            dst_binvox_path = os.path.join(vox_dest_dir, binvox_name) 
            shutil.move(binvox_path, dst_binvox_path)
            obj_path = os.path.join(parent_dir, obj_name) 
            dst_obj_path = os.path.join(mesh_dest_dir, obj_name) 
            shutil.move(obj_path, dst_obj_path)
        except:
            pass
