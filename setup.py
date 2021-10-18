import sys
from cx_Freeze import setup, Executable
import os 

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None

os.environ["tesseract-ocr"] = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Neptune",
    version = "0.1",
    description = "My GUI application!",
    options = {"build_exe": {"packages": ["tkinter","cv2","PIL","datetime","os"], "include_files":["logo.ico"]}},
    executables = [Executable("video_frame.py", base=base)]
)