#!/usr/bin/env bash

shopt -s nullglob
Xvfb :99 -screen 0 640x480x24 & export DISPLAY=:99

for i in /data/city/berlin/berlin_poly_objs/*/*.obj; do
    ./binvox -c -pb -d 256 $i
done

#for d in $(find /data/city/berlin/berlin_poly_objs/ -maxdepth 1 -type d)
#do
#  res=$( echo $d | cut -d'/' -f 7 )  # get the subfolder name only
#  src="/media/yuqiong/DATA/city/berlin/"$res  # source of citygml subfolders 
#  dst="/media/yuqiong/DATA/city/berlin_poly_objs/"$res  # destination of obj outputs
#  # echo $src
#  # echo $dst
  echo $res
#  python main.py -i $src -o $dst 
#done


