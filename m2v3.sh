#!/usr/bin/env bash
shopt -s nullglob
# Xvfb :99 -screen 0 640x480x24 & 
# export DISPLAY=:99
for i in /data/city/berlin/berlin_poly_objs/*/*.obj; do
    ./binvox -c -pb -d 256 $i
done 
