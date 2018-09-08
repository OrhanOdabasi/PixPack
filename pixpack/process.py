#!/usr/bin/env python3
# process.py
# This script consists of all core functions.
# Author: Orhan Odabasi (0rh.odabasi[at]gmail.com)

import locale
import csv
import os
from PIL import Image
import re
from collections import Counter


def scanDir(path):
    # scan the path and collect media data for copy process
    while os.path.exists(path) and os.path.isdir(path):
        photos_dataset, totalsize, folder_count, videos_dataset = listphotos(path)
        p_count = len(photos_dataset)
        p_size = "{:.2f} MB".format(float(totalsize/1000000))
        return p_count, p_size, folder_count, photos_dataset, videos_dataset

def saveReport(photo_datas, video_datas, target_path):
    # save summary data to a csv file
    report_dest_p = os.path.join(target_path, "photo_list.csv")
    report_dest_v = os.path.join(target_path, "video_list.csv")
    with open(report_dest_p, "w") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerows(photo_datas)
        f.close()
    with open(report_dest_v, "w") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerows(video_datas)
        f.close()

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
                # date taken [3]
                date_taken = Image.open(file_path)._getexif()[36867]
                # year/month/day format required
                ymd_format = re.match("(\d{4}):(\d{2}):(\d{2})", date_taken)
                # year taken [4]
                year = ymd_format.group(1)
                # month taken [5]
                month = ymd_format.group(2)
                # day taken [6]
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

            if name.lower().endswith((".jpeg", ".jpg", ".png", ".dng")):
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
