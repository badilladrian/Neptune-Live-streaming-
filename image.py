import cv2
import pytesseract
from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from pytesseract.pytesseract import Output


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = tk.Tk()

app.title('Neptune Service')
app.iconbitmap('logo.ico')
app.geometry('900x650')
app.config(bg='#2A3166')
Label(app,text="Extract Number from Image",font=("times new roman",30,"bold")).pack(pady=20)






def ImageRead():
    image = cv2.imread('0.jpg', 0)
    thresh = cv2.threshold(image, 0,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(thresh, lang='eng', config='digits')
    output.insert(END,data)
    print(data)
    messagebox.showinfo("Neptune Service","Number save in the CSV file Successfully.")

    with open('csvfile.csv', 'w') as file:
        for l in data:
            file.write(l)
            file.write('\n')


Button(app,text="Image Read",font=("times new roman",20,"bold"),bg="black",fg="red",command=ImageRead).pack(expand=True,pady=10)

Label(app,text="Number Will be displayed here.",font=("times new roman",15,"bold")).pack(pady=20)
output = Text(app, width=40, height=12)
output.pack()




#start program
app.mainloop()