#!/usr/bin/env bash
for i in /data/city/montreal/montreal_binvox/*.binvox; do
    ./v2d 1 $i /data/city/montreal/montreal_dem 1
done
