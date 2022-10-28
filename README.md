# OneClickPDF
## Windows context menu tool for converting pdf to jpg and back

- [x] Implement PDF to JPG conversion
- [x] Registry key generator for context menu
- [ ] Create windows installation package
- [ ] Implement JPG to PDF conversion


## Installation and Testing

### For Non-Contributors

- To install OneClickPDF download the repository as a .zip and extract it to your `C:\Program Files` directory.
- Ensure you have Python installed (Download the latest release (here)[https://www.python.org/downloads/]) and you know where python.exe is.
- Ensure line 13 ( the last SetValue ) in generatekeys.py show the correct location for your python.exe.  
- If you added python to your PATH you can now click on the generatekeys.py file and the registry keys will be added
- The right click context menu will now convert pdf files to jpg
  