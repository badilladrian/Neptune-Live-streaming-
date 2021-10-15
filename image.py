import cv2
import pytesseract
from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = tk.Tk()

app.title('Neptune Service')
app.iconbitmap('logo.ico')
app.geometry('800x730')
app.config(bg='#84BF04')
Label(app,text="Extract Number from Image",font=("times new roman",30,"bold")).pack(pady=20)




image = cv2.imread('1.jpg', 0)
thresh = cv2.threshold(image, 0,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
print(data)

with open('csvfile.csv', 'w') as file:
    for l in data:
        file.write(l)
        file.write('\n')


message ='''
Number Will be displied here

    '''

text_box = Text(
    app,
    height=12,
    width=40
)
text_box.pack(expand=True,)
text_box.insert('end', message)
text_box.config(state='disabled')

#start program
app.mainloop()