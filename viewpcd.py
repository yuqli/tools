import numpy as np
import os
import pptk

src = "/media/yuqiong/DATA/city/nyc/nyc_tri_pcds_sample"
allf = os.listdir(src)

for f in allf[41:]:
    print(f)
    path = os.path.join(src, f)
    dat = np.load(path)
    v = pptk.viewer(dat)
    input("Press Enter to continue...")
    v.close()
