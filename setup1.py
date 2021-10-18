import sys,os
from cx_Freeze import setup, Executable

base = None

os.environ["tesseract-ocr"] = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if sys.platform == "win32":
    base = "Win32GUI"

options = {
'build_exe': {'path': sys.path + ['modules']}
}

executables = [
    Executable('Home.py'),
    Executable('video_frame.py'),
    Executable('image.py')]

setup(
    name='two exe in one folder',
    version='0.1',
    description='Two exe in a single build folder',
    options = {"build_exe": {"packages": ["tkinter","cv2","PIL","datetime","os"], "include_files":["logo.ico"]}},
    executables=executables)