from cgitb import text
from fileinput import filename
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import cv2
# from matplotlib import pyplot as plt
# import numpy as np
import easyocr
#import pytesseract

def UploadAction():
    filename = filedialog.askopenfilename()
    #filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print('Selected File : ', filename)
    
    global fname
    fname = filename
    imgp1 = filename
    imgp = cv2.imread(imgp1)
    gray = cv2.cvtColor(imgp, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    
    global result
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(gray, detail = 0)
    messagebox.showinfo("Success","File Succesfully Uploaded")  
    result
    
def Scan(event=UploadAction):
    if (fname == None):
        print('Please Upload File First')
        messagebox.showerror("Error", "Please Upload File First")
    else:
        print("\nFile Selected : " + fname)
        print('----------------------------')
        print("Scanned ID Card")
        nik=result[3]
        nama=result[5]
        kotal=result[7]
        tanggall=result[8]
        jeniske=result[10]
        alamat=result[13]+ '  '+result[14] + '  '+result[15]+ '  '+result[16]+ '  '+result[17]+ '  '+result[18]+ '  '+result[19]
        agam=result[22]
        tempk=result[0]+', '+result[1]
        tanggalk=result[27]
        print('=================================')
        print('NIK : ' + nik)
        print('Nama : ' + nama)
        print('Kota Kelahiran : ' + kotal)
        print('Tanggal Kelahiran : ' + tanggall)
        print('Jenis Kelamin : ' + jeniske)
        print('Alamat Lengkap : ' + alamat)
        print('Agama : ' + agam)
        print('Tempat Pembuatan KTP : ' + tempk)
        print('Tanggal Pembuatan KTP : ' + tanggalk)
        print('=================================')
root = tk.Tk()

# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Label(root,text='ID Card OCR Program')
upload = tk.Button(root, text='Upload File', command=UploadAction)
scan = tk.Button(root, text='Scan Selected File', command=Scan)
exit = tk.Button(root, text="Exit", command=root.destroy)
upload.pack()
scan.pack()
exit.pack()

root.mainloop()