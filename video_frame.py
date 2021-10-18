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
app.geometry('900x700')
app.config(bg='#2A3166')
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
    i = 0
    image = Image.fromarray(img1)
    #time = str(datetime.datetime.now().today()).replace(":"," ")+".jpg"
    time = str(i) + '.jpg'
    image.save(time)
    messagebox.showinfo("Neptune Service","Image Save Successfully.")


Button(app,text="Capture",font=("times new roman",20,"bold"),bg="#23272b",fg="white",command=singlePhoto).pack(expand=True,pady=10,side = LEFT)
Button(app,text="Exit",font=("times new roman",20,"bold"),bg="#e6bc15",fg="white",command=app.destroy).pack(expand=True,pady=10,side = LEFT)






while True:
    img = cap.read()[1]
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img1))
    L1['image'] = img
    L1.pack()

    app.update()

cap.release()
#start program
app.mainloop()

