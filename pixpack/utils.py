#!/usr/bin/env python3
# utility.py
# PixPack Photo Organiser
# It contains some useful functions to increase user experience

import locale
import os


def sys_trans_var():
    # check system language
    sys_loc = locale.getlocale()
    sys_lang = sys_loc[0] # system default language
    if sys_lang == 'en_EN' or sys_lang == 'en_GB':
        return 0
    elif sys_lang == 'tr_TR':
        return 1
    else:
        return 0

def name_existing_photos(dest_directory, dest_file, copy_suffix):
    # rename if the file is existed already, for instance: photo_1
    dest_file_path = os.path.join(dest_directory, dest_file)
    i=1
    while os.path.exists(dest_file_path):
        dest_file_path = os.path.join(dest_directory, dest_file)
        file_name = os.path.basename(dest_file_path)
        name, ext = os.path.splitext(file_name)
        name = name + "_" + str(copy_suffix) + str(i)
        new_name = name + ext
        dest_file_path = os.path.join(dest_directory, new_name)
        i+=1
    return dest_file_path
