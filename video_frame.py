from tkinter import font
import cv2
from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
import datetime
from tkinter import messagebox


app = tk.Tk()

app.title('Neptune Service')
app.iconbitmap('logo.ico')
app.geometry('800x730')
Label(app,text="Live Stream",font=("times new roman",30,"bold")).pack(pady=20)
f1 = LabelFrame(app,bg="red")
f1.pack()
L1 = Label(f1,bg="red")
L1.pack()
# it will open live camera 
cap = cv2.VideoCapture(0)


# def framseve():
#     i = 0
#     while(cap.isOpened()):
#         ret , frame = cap.read()
#         if ret == False:
#             break
#         cv2.imwrite('./data/Frame'+str(i)+'.jpg', frame)
#         #print('Read a new frame: ', frame)
#         i += 1

def singlePhoto():
    image = Image.fromarray(img1)
    time = str(datetime.datetime.now().today()).replace(":"," ")+".jpg"
    image.save(time)
    messagebox.showinfo("Information","Image Save Successfully.")

login_button = ttk.Button( text="Start",command=singlePhoto)
login_button.pack(fill='x',  pady=10)

login_button = ttk.Button( text="Quit", command=app.quit())
login_button.pack(fill='x',  pady=10)




while True:
    img = cap.read()[1]
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img1))
    L1['image'] = img

    app.mainloop()

cap.release()
#start program
app.mainloop()

