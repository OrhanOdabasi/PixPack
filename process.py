#!/usr/bin/env python3
# process.py
# This script consists of all core functions.
# PixPack v2 - Organize your photos safely...
# Author: Orhan Odabasi (0rh.odabasi[at]gmail.com)

import locale
import csv
import os
import os.path
from PIL import Image
import re
from collections import Counter

# NOTE: edited
def sysTransVar():
    # check system language
    # If system language is English, returns 0
    # If Turkish, returns 1
    sys_lang = locale.getlocale()
    if sys_lang[0] == 'en_EN' or sys_lang[0] == 'en_GB':
        return 0
    elif sys_lang[0] == 'tr_TR' or sys_lang[0] is None:
        return 1
    else:
        return 0

# NOTE: edited
def scanDir(path):
    # scans the path and collects media data for copy process
    while os.path.exists(path) and os.path.isdir(path):
        photos_dataset, totalsize, folder_count, videos_dataset = listphotos(path)
        p_count = len(photos_dataset)
        p_size = "{:.2f} MB".format(float(totalsize/1000000))
        return p_count, p_size, folder_count, photos_dataset, videos_dataset

# NOTE: edited
def saveReport(photo_datas, video_datas, target_path):
    # saves summary data to a csv file
    report_dest_p = os.path.join(target_path, "photo_list.csv")
    report_dest_v = os.path.join(target_path, "video_list.csv")
    with open(report_dest_p, "w") as f:
        w = csv.writer(f, delimiter=",")
        w.writerows(photo_datas)
        f.close()
    with open(report_dest_v, "w") as f:
        w = csv.writer(f, delimiter=",")
        w.writerows(video_datas)
        f.close()

# NOTE: edited
def listphotos(path):
    # Listing all files in target directory
    photos_dataset = []
    videos_dataset = []
    for root, dirs, files in os.walk(path):
        for name in files:
            p_data_list = []
            v_data_list = []
            # filename name [0]
            file_name = name
            # file path [1]
            file_path = os.path.join(root, file_name)
            # file size [2]
            file_size = os.path.getsize(file_path)

            try:
                date_taken = Image.open(file_path)._getexif()[36867]
                # year/month/day format required
                ymd_format = re.match("(\d{4}):(\d{2}):(\d{2})", date_taken)
                year = ymd_format.group(1)
                month = ymd_format.group(2)
                day = ymd_format.group(3)
                # date info will be our new folder name
                date_info = "{0}-{1}".format(year, month)
            except:
                date_taken = "NOT_FOUND"
                day = "NOT_FOUND"
                year = "NOT_FOUND"
                month = "NOT_FOUND"
                # destination folder name [7]
                date_info = "NOT_FOUND"

            if name.lower().endswith((".jpeg", ".jpg", ".png")):
                p_data_list.extend([file_name, file_path, file_size, date_taken, year, month, day, date_info])
                photos_dataset.append(p_data_list)
            elif name.lower().endswith((".mov", ".mkv", ".mp4", ".3gp", ".wmv", ".avi")):
                v_data_list.extend([file_name, file_path, file_size, date_taken, year, month, day, date_info])
                videos_dataset.append(v_data_list)

    # total size of photos archive (only jpeg and png files)
    totalsize = 0
    for s in photos_dataset:
        totalsize += int(s[2])

    #total file count
    dirs = []
    for x in photos_dataset:
        dirs.append(x[7])

    foldercount = len(Counter(dirs).most_common())
    return photos_dataset, totalsize, foldercount, videos_dataset
