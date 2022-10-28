# -*- coding: utf-8 -*-

from pdf2image import convert_from_path as PDFConv
from pathlib import Path
import sys
import os
import ctypes

userprofile = os.environ['USERPROFILE']
CURRENT_USER_PATH = os.path.join(userprofile, 'Documents')

def ConvertPDF(pdf_path, output_folder = CURRENT_USER_PATH, poppler_path = r"C:\Program Files\oneclickPDF\poppler-22.04.0\Library\bin", saveas_seed = "PDF2IMG"):
    ctypes.windll.user32.MessageBoxW(0, "File saved to: " + CURRENT_USER_PATH, "File Converted to JPG", 1)
    converted_imgs = PDFConv(pdf_path, poppler_path = poppler_path)
    
    for i in range(len(converted_imgs)):
        converted_imgs[i].save(str(output_folder) + '\page' + str(i) + saveas_seed + '.jpg', 'JPEG')
        


if __name__=="__main__":
    ConvertPDF(sys.argv[1])
