from tkinter import font
import cv2
from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
# import os
# import sys
# import video_frame

app = tk.Tk()

app.title('Neptune Service')
app.iconbitmap('logo.ico')
app.geometry('800x500')






Label(app,text="Neptune Service",font=("times new roman",30,"bold")).pack(pady=10)


ip = tk.StringVar()
password = tk.StringVar()

# Sign in frame
signin = ttk.Frame(app)
signin.pack(padx=10, pady=10, fill='x',)


# Ip
email_label = ttk.Label(signin, text="Enter Ip:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=ip)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# Pass
email_label = ttk.Label(signin, text="Enter Password:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=password)
email_entry.pack(fill='x', expand=True)
email_entry.focus()


# def open(filename):
#     os.chdir("C:\\Users\\Mehedi\\Desktop\\machine\\") #change this path to your path where your f1.py and f2.py is located
#     # print("current dir "+os.getcwd())
#     os.system('python '+filename)


login_button = ttk.Button(signin, text="Start",command=lambda: open("video_frame.py"))
login_button.pack(fill='x', expand=True, pady=10)

login_button = ttk.Button(signin, text="Quit", command=app.quit)
login_button.pack(fill='x', expand=True, pady=10)




#start program
app.mainloop()