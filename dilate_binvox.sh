#!/usr/bin/env bash
mkdir /media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample_64
mkdir /media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample_log
python resolute_binvox.py --input_dir "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample" --output_dir "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample_64" --log_dir "/media/yuqiong/DATA/city/nyc/nyc_poly_binvox_sample_log"