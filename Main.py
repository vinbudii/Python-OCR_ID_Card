from asyncio.windows_events import NULL
import imp
import cv2
import easyocr
import tkinter as tk
from cgitb import text
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from fileinput import filename
from PIL import Image, ImageTk

root = tk.Tk()

def UploadAction():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg"),("all files","*.*")))
    print('Selected File : ', filename)
    
    global flag
    flag = filename
    fname = filename
    fname = cv2.imread(fname)
    gray = cv2.cvtColor(fname, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    
    global result
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(gray, detail = 0)
    messagebox.showinfo("Success",filename +" \n\nFile Succesfully Uploaded")  
    result
    
def Scan():
    try:
        result
    except NameError:
        print('Please Upload File First')
        messagebox.showerror("Error", "Please Upload File First")
    else:
        global i
        i=+1
        coun = '=========\n'+'No. '+str(i) +'\n'
        filesel = '\nFile Selected : '+ flag + '\n'
        nik=result[3]
        nama=result[5]
        kotal=result[7]
        tanggall=result[8]
        jeniske=result[10]
        alamat=result[13]+ '  '+result[14] + '  '+result[15]+ '  '+result[16]+ '  '+result[17]+ '  '+result[18]+ '  '+result[19]
        agam=result[22]
        tempk=result[0]+', '+result[1]
        tanggalk=result[27]
        extract='NIK : ' + nik +'\n'+'Nama : ' + nama + '\n' + 'Kota Kelahiran : ' + kotal + '\n' + 'Tanggal Kelahiran : ' + tanggall + '\n'+'Jenis Kelamin : ' + jeniske + '\n'+ 'Alamat Lengkap : ' + alamat +'\n'+ 'Agama : ' + agam +'\n' + 'Tempat Pembuatan KTP : ' + tempk +'\n'+ 'Tanggal Pembuatan KTP : ' + tanggalk
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, filesel+extract)
        text_box.pack()
        
logo = Image.open('./logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.pack()
upload = tk.Button(root, text='Upload File', command=UploadAction)
scan = tk.Button(root, text='Scan Selected File', command=Scan)
exit = tk.Button(root, text='Exit', command=root.destroy)
upload.pack()
scan.pack()
exit.pack()

root.mainloop()