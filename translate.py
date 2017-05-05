# translate.py
#!/usr/bin/env python3
# This is a json generator script for translate.json
# PixPack v2 - Organize your photos safely...
# Author: Orhan Odabasi (0rh.odabasi[at]gmail.com)

import json

# notification code: 2
# success code: 1
# fail code: 0

trans = {

    "title": ["PixPack - Organize your photos safely...",
               "PixPack - Fotoğraflarınızı güvenle düzenleyin..."],
    "about_menu": ["About",
                  "Hakkında"],
    "help_menu" : ["Help",
                  "Yardım"],
    "intro_label": ["You can put your photos into folders by date information!",
                    "Fotoğraflarınızı tarih sırasına göre gruplayabilirsiniz!"],
    "scan_label" : ["Scanning",
                    "Tarama"],
    "path_label": ["Folder Path of Your Photos:",
                   "Fotoğrafların Klasör Adresi:"],
    "save_check": ["Create a CSV report file for this process",
                  "Bu işlemle ilgili CSV raporu oluştur"],
    "scan_bttn": ["Scan",
                  "Tara"],
    "stats_label": ["Statistics",
              "İstatistikler"],
    "pcount_label": ["Photos to be Organized:",
                     "Düzülecek Foto Sayısı:"],
    "psize_label": ["Total Size (MB):",
                    "Toplam Boyut (MB):"],
    "fcount_label": ["Folders to be Created:",
                     "Oluşturulacak Klasör Sayısı:"],
    "pathout_label": ["Output Directory:",
                      "Hedef Klasör Yolu:"],
    "start_bttn": ["Start Organizing",
                   "Düzmeye Başla"],
    "proc_label": ["Process:",
                   "İşlem >"],
    "prog_info": ["PixPack - Photo Archive Program",
                  "PixPack - Resim Arşivleme Programı"],
    "programmer": ["Written by Orhan Odabasi",
                   "Orhan Odabaşı tarafından yazıldı."],
    "contact": ["Contact: 0rh.odabasi@gmail.com",
                "İletişim: 0rh.odabasi@gmail.com"],
    "prog_lang": ["Programming Language: Python (v3.5)",
                  "Programlama Dili: Python (v3.5)"],
    "proc_NA": ["Ready to scan!",
                "Tarama işlemine hazır!"],
    "proc_scan": ["Scanning started. Please wait...",
                  "Tarama başladı. Lütfen bekleyin..."],
    "proc_blankpath": ["ERROR: Invalid or missing folder path!",
                       "HATA: Eksik ya da yanlış dosya yolu!"],
    "proc_saveTrue": ["Report was save successfully. Ready to Organize!",
                      "Rapor başarıyla kaydedildi. Düzme işlemi hazır!"],
    "proc_saveFalse": ["Report was NOT saved. Ready to organize!",
                       "Rapor kaydedilMEdi. Düzme işlemi hazır!"],
    "process": ["Please wait! Process continues...",
                "Lütfen bekleyin! İşlem devam ediyor..."],
    "proc_ok": ["Organize process completed successfully!",
                "Düzme işlemi başarıyla tamamlandı!"],
    "proc_fail": ["ERROR: Process failed!",
                  "HATA: İşlem başarısız!"],
    "proc_NULL": ["You should scan a folder path first!",
                  "Önce bir dosya yolunu taramalısınız!"],
    "copy": ["pCopy",
             "pKopya"]
}

with open('translate.json', 'w') as f:

    json.dump(trans, ensure_ascii=False, fp=f, indent=4)
    f.close()