import os
import sys
import winreg

KEY_PATH = r"Directory\Background\shell\oneclickPDF"


def main():
    topkey = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, KEY_PATH)
    winreg.SetValue(topkey, '', winreg.REG_SZ, '&oneclickPDF')
    winreg.SetValue(topkey, 'Icon', winreg.REG_SZ, "C:\Program Files\oneclickPDF\OCIcon.png")
    commandkey = winreg.CreateKeyEx(topkey, r"command")
    winreg.SetValue(commandkey,'', winreg.REG_SZ, "C:\Program Files\oneclickPDF\converterApp.py" + "%1")

if __name__=="__main__":
    main()