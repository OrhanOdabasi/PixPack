# PixPack Photo Organiser v1.2

![PixPack Showcase](https://1.bp.blogspot.com/-orCPq1IU72Y/WRiELaHW9_I/AAAAAAAAOd0/VW9kEhVOvmk8jQnFsz14LFrIIuTHbEpbQCLcB/s1600/pixpackv2.png)

PixPack is a photo organiser application which is designed with Qt Designer 4
and written in Python 3 and is available on Linux operating systems. So far,
options are limited but it will be developed frequently. Here are some of the features:


* Scans the specified directory and creates a report file which lists all supported
images and videos in it.
* It groups images by their taken dates and copies wherever you would like to.
* You can group your photos by year (2017), year-month couple (2017-03) or season
(WINTER) for now. Other sorting algorithms will be added soon.
* It **DOES NOT** erase any of the original files and **DOES NOT** lose metadata while copy process.
* If there is any image or video exists in the target directory, it separates the
duplicated ones in a folder called "copies".

## Supported File Formats

Image Types: JPEG, PNG, DNG
Video Types: MOV, MKV, MP4, 3GP, WMV, AVI


### Notes:


*If target directory is empty, source directory will be set as target directory.*

*If any word or phrase is entered in target directory field, target folder name will
be the word/phrase in source directory.*

*'shutil.copy2' method was used in the script, so any metadata in the image/video
will be preserved.*


## Screenshots

![Just Before Start-Up](https://3.bp.blogspot.com/-oocUWYEW40s/WRh9sBukzWI/AAAAAAAAOdg/GnlTyMCos2EQrnRyq6zNXDS-rZlWo1ERQCLcB/s1600/pixpack1.png)
![PixPack on Action](https://3.bp.blogspot.com/-WoR7EHaVce8/WRh-IncDKuI/AAAAAAAAOdk/t0mACs2g98cjsuFVll4DLK490QaE7QvqQCLcB/s1600/action.png)


## Installation


You should have super user privileges while installing or uninstalling:

Installation:
```sh
git clone https://github.com/OrhanOdabasi/PixPack.git
cd PixPack
sudo make install
```

Uninstallation:
```sh
sudo make uninstall
```

Update:
```sh
sudo make update
```


## Dependencies


For now, you should install all the dependencies manually via apt package manager
or pip Python package manager.


* Python 3.5 or above
* PyQt 5.8.2
* Pillow 4.1.1


#### Installing Dependencies


with apt package manager:
```sh
sudo apt install python3-pyqt5 python3-pil
```

with pip Python package manager
```sh
pip3 install pyqt5
pip3 install pillow
```


## Test Environments


tested on: Netrunner 17.03 KDE Plasma, Debian 9.4.0 Gnome, Kali 2017.1 Gnome, Solus OS Budgie, Pop OS.



#### Copyright

MIT Licence 2017 - Orhan Odabasi
