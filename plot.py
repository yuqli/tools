#!/usr/env/bin python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def parse_obj(path):
    """
    a function to read and parse obj files
    @ param path: absolute path to obj file
    rvalue:
    - all_v : list of lists, all vertice coordinates
    - all_f: list of lists, all faces. each face consists of vertice ID
    """
    with open(path) as fp:
        lines = fp.readlines()
    lines = [x for x in lines if x[0] != '#']
    # handling all vertices
    all_v = [x.split(' ')[1:] for x in lines if x[0] == 'v'] # all verices
    new_vs = []
    for v in all_v:
        v = [float(x.strip()) for x in v]
        new_vs.append(v)

    # handling all faces
    all_f = [x.split(' ')[1:] for x in lines if x[0] == 'f'] # all verices
    new_fs = []
    for f in all_f:
        f = [int(x.strip()) for x in f]
        new_fs.append(f)
    return new_vs, new_fs


# dat = [[ -9.5259,    -0.621975],
#  [ -4.6457,   -11.685875],
#  [ -3.6021,     1.991025],
#  [ -3.1121,     0.880025],
#  [  2.1561,     4.755125],
#  [  2.7289,     3.456425],
#  [  5.5189,     6.238425],
#  [ 10.4819,    -5.013175]]
# path = "gml_U2VLBZW4J9D0HX2928ZQNTL7B3UG372N5QUM.obj"
# v_list, f_list = parse_obj(path)
# v_list = [[-9.525900000415277, -0.6219750022064545, -3.2527711455411934], [-9.525900000415277, -0.6219750022064545, 3.252771145541197], [-4.645700003369711, -11.685875001705426, -3.2527711455411934], [-4.645700003369711, -11.685875001705426, 3.252771145541197], [-3.6020999993779697, 1.9910250013926998, -3.2527711455411934], [-3.6020999993779697, 1.9910250013926998, 3.252771145541197], [-3.112100000376813, 0.8800249971973244, -3.2527711455411934], [-3.112100000376813, 0.8800249971973244, 3.252771145541197], [2.156100000604056, 4.755125000694534, -3.2527711455411934], [2.156100000604056, 4.755125000694534, 3.252771145541197], [2.72889999859035, 3.456424999596493, -3.2527711455411934], [2.72889999859035, 3.456424999596493, 3.252771145541197], [5.518900002585724, 6.23842500209139, -3.2527711455411934], [5.518900002585724, 6.23842500209139, 3.252771145541197], [10.481900001585018, -5.013174997104215, -3.2527711455411934], [10.481900001585018, -5.013174997104215, 3.252771145541197]]
#
# f_list = [[15, 3, 1, 5, 7, 11, 9, 13], [11, 12, 10, 9], [15, 16, 4, 3], [3, 4, 2, 1], [5, 6, 8, 7], [9, 10, 14, 13], [1, 2, 6, 5], [13, 14, 16, 15], [7, 8, 12, 11], [16, 14, 10, 12, 8, 6, 2, 4]]


# dat = [[10.481900001585018, -5.013174997104215, -3.2527711455411934], [-4.645700003369711, -11.685875001705426, -3.2527711455411934], [-9.525900000415277, -0.6219750022064545, -3.2527711455411934], [-3.6020999993779697, 1.9910250013926998, -3.2527711455411934], [-3.112100000376813, 0.8800249971973244, -3.2527711455411934], [2.72889999859035, 3.456424999596493, -3.2527711455411934], [2.156100000604056, 4.755125000694534, -3.2527711455411934], [5.518900002585724, 6.23842500209139, -3.2527711455411934]]

# # dat = [[ -9.5259,    -0.621975],
#  [ -4.6457,   -11.685875],
#  [ -3.6021,     1.991025],
#  [ -3.1121,     0.880025],
#  [  2.1561,     4.755125],
#  [  2.7289,     3.456425],
#  [  5.5189,     6.238425],
#  [ 10.4819,    -5.013175]]


dat = [[ 10.4819,    -5.013175],
 [  5.5189,     6.238425],
 [  2.1561,     4.755125],
 [  2.7289,     3.456425],
 [ -3.1121,     0.880025],
 [ -3.6021,     1.991025],
 [ -9.5259,    -0.621975],
 [ -4.6457,   -11.685875]]

# print(v_list)
# print(f_list)
# dat = v_list
x = [d[0] for d in dat]
y = [d[1] for d in dat]
# z = [d[2] for d in dat]

plt.plot(x,y, 'ro')
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(x, y, z)

def connectpoints3D(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    z1, z2 = z[p1], z[p2]
    ax.plot([x1,x2],[y1,y2], [z1,z2], 'k-')

def connectpoints2D(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2], 'k-')
# for j in range(len(f_list)):
    # face = f_list[j]
# for i in range(len(face)-1):
#     connectpoints3D(x,y,face[i]-1,face[i+1]-1)
# connectpoints3D(x,y,face[i]-1,face[i+1]-1)

# for i in range(len(dat)-1):
#     connectpoints3D(x,y, i, i+1)
# connectpoints3D(x,y,len(dat)-1,0)

for i in range(len(dat)-1):
    connectpoints2D(x,y, i, i+1)
connectpoints2D(x,y,len(dat)-1,0)

plt.axis('equal')
plt.show()
