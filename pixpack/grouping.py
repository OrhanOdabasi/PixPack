#!/usr/bin/env python3
# grouping algorithms for images and videos
# PixPack Photo Organiser

import re
import os

def group_by_dates(date_meta, destination, pattern='ym'):
    # generate folder name by using basic date informations
    # available patterns: yr=2017, ym=2017-03, ss=summer
    # exif date format -> 2006:03:25 21:34:24
    # return dest_dir
    if date_meta == "NOT_FOUND":
        return os.path.join(destination, "NOT_FOUND")
    ymd_format = re.match(r"(\d{4}):(\d{2}):(\d{2}) (\d{2}):(\d{2}):(\d{2})", date_meta)
    year = ymd_format.group(1)
    month = ymd_format.group(2)
    day = ymd_format.group(3)
    hour = ymd_format.group(4)
    minute = ymd_format.group(5)
    second = ymd_format.group(6)
    # group by year
    if pattern.lower() == 'yr':
        dest_folder_name = year
    elif pattern.lower() == 'ym':
        dest_folder_name = "{year}-{month}".format(year=year, month=month)
    elif pattern.lower() == 'ss':
        if int(month) in (12, 1, 2):
            dest_folder_name = "Winter"
        elif int(month) in (3, 4, 5):
            dest_folder_name = "Spring"
        elif int(month) in (6, 7, 8):
            dest_folder_name = "Summer"
        elif int(month) in (9, 10, 11):
            dest_folder_name = "Fall"
    return os.path.join(destination, dest_folder_name)
