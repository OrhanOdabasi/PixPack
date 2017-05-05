#!/usr/bin/env python3
# process.py
# This script consists of all basic processes.
# PixPack v2 - Organize your photos safely...
# Author: Orhan Odabasi (0rh.odabasi[at]gmail.com)

import locale
import csv
import os
import os.path
from PIL import Image
import re
from collections import Counter


def sysTransVar():
    
    # check system language
    sys_lang = locale.getlocale()
    if sys_lang[0] == 'en_EN' or sys_lang[0] == 'en_GB' :
        return 0
    elif sys_lang[0] == 'tr_TR' or sys_lang[0] is None:
        return 1

def saveReport(photo_datas, target_path):

    # save these infos to a csv file
    report_dest = os.path.join(target_path, "photo_list.csv")
    with open(report_dest, "w") as f:
        w = csv.writer(f, delimiter=",")
        w.writerows(photo_datas)
        f.close()

def scanDir(path):

    # scan process
    while os.path.exists(path) and os.path.isdir(path):
        photos_dataset, totalsize, folder_count = listphotos(path)
        p_count = len(photos_dataset)
        p_size = "{:.2f} MB".format(float(totalsize/1000000))
        return p_count, p_size, folder_count, photos_dataset

def listphotos(path):
    # Listing all files in target directory
    photos_dataset = []

    for root, dirs, files in os.walk(path):

        for name in files:
            data_list = []
            # picking only jpg and png files
            if name.lower().endswith((".jpeg", ".jpg", ".png")):

                # photo's name [0]
                file_name = name
                data_list.append(file_name)

                # photo's path [1]
                file_path = os.path.join(root, file_name)
                data_list.append(file_path)

                # photo's size [2]
                file_size = os.path.getsize(file_path)
                data_list.append(file_size)

                # finding out when it was taken (exifcode=36867)
                # http://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif/datetimeoriginal.html
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
                    year = "NOT_FOUND"
                    month = "NOT_FOUND"
                    date_info = "NOT_FOUND"
                    day = "NOT_FOUND"

                # photo's full date info [3]
                data_list.append(date_taken)

                # photo's year [4]
                data_list.append(year)

                # photo's month [5]
                data_list.append(month)

                #photo's day [6]
                data_list.append(day)

                # where it will be moved/new folder name [7]
                data_list.append(date_info)
                photos_dataset.append(data_list)



    # total size of photos archive (only jpeg and png files)
    totalsize = 0
    for s in photos_dataset:
        totalsize += int(s[2])

    #total file count
    dirs = []
    for x in photos_dataset:
        dirs.append(x[7])

    foldercount = len(Counter(dirs).most_common())

    return photos_dataset, totalsize, foldercount

"""
def bttf(destination, photodata, copy_suffix):
    # copy process
    for x in photodata:

        dest_dir = os.path.join(destination, str(x[7]))
        if os.path.exists(dest_dir):
            dest_file = os.path.join(dest_dir, x[0])
            i = 1
            while os.path.exists(dest_file):
                dest_file = os.path.join(dest_dir, x[0])
                base_name = os.path.basename(dest_file)
                name, ext = os.path.splitext(base_name)
                name = name + "_" + str(copy_suffix) + str(i)
                base_name = name + ext
                dest_file = os.path.join(os.path.dirname(dest_file), base_name)
                i += 1
            shutil.copy2(x[1], dest_file)
        else:
            os.makedirs(dest_dir)
            shutil.copy2(x[1], dest_dir)
"""
