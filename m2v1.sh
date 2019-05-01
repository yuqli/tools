#!/usr/bin/env bash
shopt -s nullglob
Xvfb :99 -screen 0 640x480x24 & 
export DISPLAY=:99
while IFS='' read -r line || [[ -n "$line" ]]; do
    # echo "Text read from file: $line"
    ./binvox -c -pb -d 256 "/data/city/zurich/zurich_new_objs/"$line
done < "/data/city/zurich/undone_objs.txt" 

# for i in /data/city/nyc/nyc_poly_objs/*.obj; do
#    ./binvox -c -pb -d 256 $i
# done 
