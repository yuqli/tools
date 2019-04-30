import numpy as np
import os
import pptk

# p1 = "/media/yuqiong/DATA/city/nyc/nyc_tri_pcds_sample_2048"
p2 = "/media/yuqiong/DATA/city/nyc/nyc_tri_pcds_4096_sample"

# allf1 = os.listdir(p1)
allf2 = os.listdir(p2)
# allf = list(set(allf1) & set(allf2))

for f in allf2:
    print(f)
    path = os.path.join(p2, f)
    dat = np.load(path)
    v = pptk.viewer(dat)
    input("Press Enter to continue...")
    v.close()

    # path = os.path.join(p2, f)
    # dat = np.load(path)
    # v = pptk.viewer(dat)
    # input("Press Enter to continue...")
    # v.close()
