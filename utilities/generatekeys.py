import os
import sys
import winreg

KEY_PATH = r"*\shell\oneclickPDF"


def main():
    topkey = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, KEY_PATH)
    winreg.SetValue(topkey, '', winreg.REG_SZ, '&oneclickPDF')
    winreg.SetValueEx(topkey, 'Icon', '', winreg.REG_SZ, "C:\Program Files\oneclickPDF\OCIcon.ico")
    commandkey = winreg.CreateKeyEx(topkey, r"command")
    winreg.SetValue(commandkey,'', winreg.REG_SZ, "\"C:\Python310\python.exe\"" +" "+ "\"C:\Program Files\oneclickPDF\converterApp.py\"" +" "+ "\"%1\"")

if __name__=="__main__":
    main()