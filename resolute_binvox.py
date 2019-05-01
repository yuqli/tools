### 20190430
### resolute binvox to lower resolution

import os
import numpy as np
import binvox_rw
import argparse
import time



def log_error(error_log, f):
    """
    log error to a file
    :param error_log: path to error log. ends with ".txt"
    :param f: obj file name
    :return:
    """
    with open(error_log, "a+") as e:
        e.write(f)
    return


def dilate(volume, target_dim, thres):
    """
    dilate a higher dimension volume to lower dimension
    :param volume: 3D numpy array
    :param target_dim: target dimension
    :param thres: threshold of how many voxel fills count as one. float between 0 and 1
    :return: 3D numpy array of shape target_dim ** 3
    """
    src_dim = volume.shape[0]
    cube_dim = int(src_dim / target_dim)  # dimension of the small cube
    thres_num = int(cube_dim ** 3 * thres)

    newv = np.empty([target_dim, target_dim, target_dim])   # empty voxel to fill
    for x in range(target_dim):
        sx = cube_dim * x   # starting x
        ex = cube_dim * (x+1)  # ending x, not included in indexing
        for y in range(target_dim):
            sy = cube_dim * y   # starting y
            ey = cube_dim * (y+1)  # ending y
            for z in range(target_dim):
                sz = cube_dim * z   # starting z
                ez = cube_dim * (z+1)  # ending z
                cube = volume[sx:ex, sy:ey, sz:ez]   # sub cube of data
                if np.sum(cube) >= thres_num:
                    newv[x, y, z] = 1
                else:
                    newv[x, y, z] = 0
    return newv


def main(args):
    input_dir = args.input_dir
    output_dir = args.output_dir
    log_dir = args.log_dir
    error_log = os.path.join(log_dir, "error.txt")
    target_dim = 64

    allf = os.listdir(input_dir)
    start = time.time()
    for i, f in enumerate(allf):
        if (i % 1000 == 0):
            print("Now checking the {0}-th file. Elapsed time {1:.2f} min.".format(i, (time.time() - start) / 60))
        with open(os.path.join(input_dir, f), "rb") as b:
            model = binvox_rw.read_as_3d_array(b)
            volume = np.asarray(model.data*1, dtype=np.float32)
        # print("the shape of volume")
        # print(volume.shape)
        if np.sum(volume) == 0:
            print("Empty voxel! Logging...")
            log_error(error_log, f)
            continue
        else:
            newv = dilate(volume, target_dim, 0.5)
            outpath = os.path.join(output_dir, f.split(".")[0]+".npy")
            np.save(outpath, newv)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # dir parameters
    parser.add_argument('--output_dir', type=str, default="../output",
                        help='output path')
    parser.add_argument('--input_dir', type=str, default='../input',
                        help='input path')
    parser.add_argument('--log_dir', type=str, default='/log/',
                        help='for tensorboard log path save in output_dir + log_dir')

    args = parser.parse_args()
    main(args)