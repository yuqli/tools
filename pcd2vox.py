import numpy as np
import os
import pptk
import open3d
from pyntcloud import PyntCloud
import matplotlib.pyplot as plt
import time
import multiprocessing


def chunkify(lst, n):
    return [lst[i::n] for i in range(n)]


def fanout_file_list(dir, num):
    """
    fanout all files to read, return a dictionary
    :param dir:
    :param num:
    :return:
    """
    allf = os.listdir(dir)
    children = chunkify(allf, num)
    return children


def worker(i, dir, dst, children):
    """
    the i-ther worker's work!
    :param i:
    :return:
    """
    print("Worker {0} started!".format(i))
    child = children[i]
    start = time.time()
    for j, f in enumerate(child):
        if (j % 1000 == 0):
            print("Worker {0}; File {1}. Elapsed time {2:.2f} min.".format(i, j, (time.time() - start) / 60))
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
        np.save(os.path.join(dst, f.split(".")[0] + ".npy"), canvas)


def main():
    dir = "/media/yuqiong/DATA/city/shapenet"
    dst = "/media/yuqiong/DATA/city/shapenet_vox"
    if not os.path.exists(dst):
        os.mkdir(dst)

    num = 20
    children = fanout_file_list(dir, num)

    # multiprocessing starts
    jobs = []
    for i in range(num):
        p = multiprocessing.Process(target=worker, args=(i, dir, dst, children))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    return

if __name__ == '__main__':
    main()
