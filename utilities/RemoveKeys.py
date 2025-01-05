import os
import sys
import winreg

KEY_PATH = r"*\shell"


def main():
    openedkey = winreg.OpenKeyEx(winreg.HKEY_CLASSES_ROOT, KEY_PATH)
    try:
        winreg.DeleteKeyEx(openedkey, r"oneclickPDF\command")
    except OSError as error:
        print(error)
    try:
        winreg.DeleteKey(openedkey, r"oneclickPDF")
    except OSError as error:
        print(error)
    
if __name__=="__main__":
    main()