# 🚀 **ChillClean**  

This script was created in the simplest way possible to help with administrative tasks. I wasn’t planning to upload it, but after setting it up for my dad and some friends, it helped them save those precious seconds... 😆  

## ✨ **Features**  
- 🗑️ **Automatically deletes** all files and folders within the specified paths.  
- ♻️ **Empties the Recycle Bin**.  

## ⚙️ **Installation & Usage**  
1. 📌 Make sure you have **Python 3.11+** installed.  
2. 📦 Install the required dependencies. The `os`, `shutil`, and `ctypes` libraries are usually included with Python, but you need to install `winshell`:  
   ```bash
   pip install winshell
   ```  
3. 📂 Modify the paths to your preference or add new ones. Example:  
   ```python
   ruta_descargas = "C:\\Users\\server\\Downloads"
   ```  
4. 🏷️ Call the new variables using the function:  
   ```python
   eliminar_contenido(ruta_descargas)
   ```  

## 🖥️ **Compile to .exe**  
If you want to convert the script into an .exe file, use **PyInstaller**:  
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --uac-admin delete.py
```  
📁 The executable will be generated in the **dist/** folder.  

## ⚠️ **Notes**  
- 🔹 There are two versions of the code:  
  - **delete.py** 🛑 Includes a condition to prevent accidental execution without admin permissions.  
  - **delete2.py** ⚡ Skips the admin check and deletes files directly.  
- ❌ **Deleted files cannot be recovered, use with caution.**
