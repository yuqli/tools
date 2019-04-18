#!/usr/bin/env python
import os
import numpy as np
import pptk

# root = "/media/yuqiong/DATA/city/nyc/nyc_pcds_from_triangle_sample"
# root = "/media/yuqiong/DATA/city/zurich/test_pcds"
root = "/data/city/nyc/nyc_poly_objs"
all_f = os.listdir(root)

for i in range(10):
    path = os.path.join(root, all_f[i])
    p = np.load(path)
    v = pptk.viewer(p)
