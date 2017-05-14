#!/bin/bash
# PyQt5 script

echo "PyDesigner dosyasının adını giriniz: "
read dosya_adi
pyuic5 $dosya_adi -o "ui.py"
