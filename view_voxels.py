### 190430
### a tool to view voxels using matplotlib

import matplotlib.pyplot as plt
import numpy as np
import os
import binvox_rw
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def read_binvox(path):
    """
    read a binvox file and return numpy array!
    :param path: path. ends with ".binvox"
    :return: numpy array of True and False
    """
    with open(path, 'rb') as b:
        model = binvox_rw.read_as_3d_array(b)
    return model.data


def read_numpy(path):
    """
    read a binvox file and return numpy array!
    :param path: path. ends with ".binvox"
    :return: numpy array of True and False
    """
    return np.load(path)


def read_bin(path):
    """
    read binary files
    :param path:
    :return:
    """
    return np.fromfile(path, dtype=np.uint8)


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


# dir1 = "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample"
# dir2 = "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample"
# path = os.path.join(dir1, os.listdir(dir1)[0])
# path = "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample_64/gml_ZZRLKXYFTBILIEWR469RSCWWSE5S793VVWKH.npy"
# path = "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample_64/gml_HUYQNNGN9TJJR5A243H07CIRB08EYJEXTUE3.npy"


# path = "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample_64_cuda/gml_I237IXUULHQUTFNYM5KJLQTNOF0XYF1D36PG.bin"
# path = "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample_64_cuda/gml_ZZH8UVEPJGVEON2A6OR03XP5HNZXYBKAHH7H.bin"
path = "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample_64_cuda/gml_ZYGT0MRS1VZ08H93AGAJ043493KLIFP82Q1B.bin"
data = read_bin(path)
print(data)
print(data.shape)

data = data.reshape(64, 64, 64)
plot_3D_voxel(data)
