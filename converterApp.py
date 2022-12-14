# -*- coding: utf-8 -*-

from pdf2image import convert_from_path as PDFConv
from pathlib import Path
from PIL import Image
import img2pdf
from random import randrange
import sys
import os
import ctypes



userprofile = os.environ['USERPROFILE']
CURRENT_USER_PATH = os.path.join(userprofile, 'Documents', 'OneClickPDF')

def ConvertPDF(pdf_path, output_folder = CURRENT_USER_PATH, poppler_path = r"C:\Program Files\oneclickPDF\poppler-22.04.0\Library\bin", saveas_seed = "PDF2IMG"):
    # Function to convert PDFs to images
    converted_imgs = PDFConv(pdf_path, poppler_path = poppler_path)
    
    # This loop converts every page of the PDF into an image
    for i in range(len(converted_imgs)):
        converted_imgs[i].save(str(output_folder) + '\page' + str(i) + saveas_seed + str(randrange(0, 10000)) + '.jpg', 'JPEG')
    
    # Tell the user where the file was saved
    ctypes.windll.user32.MessageBoxW(0, "File saved to: " + CURRENT_USER_PATH, "File Converted to JPG", 1)

def ConvertIMG(img_path, output_folder = CURRENT_USER_PATH, saveas_seed = "IMG2PDF"):
    # Function to convert images to PDFs
    
    # Open image
    img = Image.open(img_path)

    # Save the image as a pdf
    img.save(str(output_folder) + '\\' + saveas_seed + str(randrange(0, 10000)) + '.pdf', "PDF", resolution=100.0)

    # Tell the user where the file was saved
    ctypes.windll.user32.MessageBoxW(0, "File saved to: " + CURRENT_USER_PATH, "File Converted to PDF", 1)

if __name__=="__main__":
    try:
        os.mkdir(CURRENT_USER_PATH)
    except OSError as error:
        print(error)
        
    getextension = os.path.splitext(sys.argv[1])
    fileextension = getextension[1]

    if fileextension == ".pdf":
        print("Converting PDf")
        ConvertPDF(sys.argv[1])
    elif fileextension == ".jpg" or fileextension == ".png" or fileextension == ".jpeg":
        print("Converting Image (JPG or PNG)")
        ConvertIMG(sys.argv[1])
    else:
        print("Not a valid file extension for conversion")