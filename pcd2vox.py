import numpy as np
import os
import pptk
import open3d
from pyntcloud import PyntCloud
import matplotlib.pyplot as plt
import time

def plot_3D_voxel(v):
    """
    plot 3D voxels using matplotlib
    :param v: 3D numpy array
    :return:
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(v, edgecolor='k')
    plt.show()
    return


dir = "/media/yuqiong/DATA/city/shapenet"
dst = "/media/yuqiong/DATA/city/shapenet_vox"
if not os.path.exists(dst):
    os.mkdir(dst)

allf = os.listdir(dir)

start = time.time()
for i, f in enumerate(allf):
    if (i % 1000 == 0):
        print("Now moving the {0}-th file. Elapsed time {1:.2f} min.".format(i, (time.time() - start)/60))
    # print(f)
    path = os.path.join(dir, f)
    cloud = PyntCloud.from_file(path)
    voxelgrid_id = cloud.add_structure("voxelgrid", n_x=64, n_y=64, n_z=64)
    voxelgrid = cloud.structures[voxelgrid_id]
    voxelgrid.plot(d=3, mode="density", cmap="hsv")
    # print(voxelgrid.x_y_z)
    # print(voxelgrid.voxel_x)
    # print(len(voxelgrid.voxel_x))
    # print(voxelgrid.voxel_y)
    # print(len(voxelgrid.voxel_y))
    # print(voxelgrid.voxel_z)
    # print(len(voxelgrid.voxel_z))
    # print(voxelgrid.n_voxels)

    canvas = np.zeros((64, 64, 64))
    idx = np.array(voxelgrid.voxel_x)
    idy = np.array(voxelgrid.voxel_y)
    idz = np.array(voxelgrid.voxel_z)
    indexes = (idx, idy, idz)
    canvas[indexes] = 1
    # plot_3D_voxel(canvas)
    # print(canvas)
    # path = os.path.join(p2, f)
    # dat = np.load(path)
    # v = pptk.viewer(dat)
    # input("Press Enter to continue...")
    np.save(os.path.join(dst, f.split(".")[0]+".npy"), canvas)