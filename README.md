# OneClickPDF
## Windows context menu tool for converting pdf to jpg and back

![image](https://img.shields.io/badge/Version-1.1-green)

- [x] Implement PDF to JPG conversion
- [x] Registry key generator for context menu
- [x] Implement JPG to PDF conversion
- [x] Add key/file deletion script (For uninstallation)
- [ ] Create windows installation package



## Installation and Testing

### For Non-Contributors

- To install OneClickPDF download the repository as a .zip and extract it to your `C:\Program Files` directory.
- Ensure you have Python installed (Download the latest release (here)[https://www.python.org/downloads/]) and you know where python.exe is.
- Ensure line 13 ( the last SetValue ) in generatekeys.py shows the correct location for your python.exe.  
- Install the requirements to your local installation (or chosen env) using the command `pip install -r C:\Program Files\oneclickPDF\requirements.txt`
- Run the `C:\Program Files\oneclickPDF\generatekeys.py`
- The context menu should now be ready to use.
  

### For Contributors

- Just fork and clone
- Make sure the directories in generate keys are correct (If you don't want to change them you can just copy the folder to `C:\Program Files`)
- Make sure the python path in generate keys shows the correct location for your python.exe
