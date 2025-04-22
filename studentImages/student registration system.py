from tkinter import *
from datetime import date
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl
from openpyxl import Workbook
import pathlib

# ---------- COLORS & STYLES ----------
background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

# ---------- WINDOW SETUP ----------
root = Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=background)

# ---------- Paths ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(BASE_DIR, "images")
EXCEL_PATH = os.path.join(BASE_DIR, "student_data.xlsx")

# ---------- EXCEL FILE CHECK ----------
file = pathlib.Path(EXCEL_PATH)

if not file.exists():
    wb = Workbook()
    sheet = wb.active
    sheet.title = "StudentData"

    sheet['A1'] = "Registration No"
    sheet['B1'] = "Name"
    sheet['C1'] = "Class"
    sheet['D1'] = "Gender"
    sheet['E1'] = "DOB"
    sheet['F1'] = "Date of Registration"
    sheet['G1'] = "Religion"
    sheet['H1'] = "Skill"
    sheet['I1'] = "Father Name"
    sheet['J1'] = "Mother Name"
    sheet['K1'] = "Father's Occupation"
    sheet['L1'] = "Mother's Occupation"

    wb.save(EXCEL_PATH)



#gender
def selection():
    value = radio.get()
    if value == 1:
        gender = "Male"
        print(gender)
    else:
        gender = "Female"
        print(gender)
    






# ---------- EMAIL BAR ----------
Label(root, text="Email: hudsonnbenhuraa@gmail.com", bg="#f0687c",
      anchor='e', fg='white', font='arial 12', height=2).pack(side=TOP, fill="x")

# ---------- HEADER ----------
header_frame = Frame(root, bg="#c36464", height=80)
header_frame.pack(side=TOP, fill="x")

title_frame = Frame(header_frame, bg="#c36464")
title_frame.pack(side=LEFT, padx=190)  # ← Adjusted this from 20 to 90

Label(title_frame, text="STUDENT REGISTRATION", bg="#c36464", fg='white',
      font='arial 20 bold', height=2).pack()

search_frame = Frame(header_frame, bg="#c36464")
search_frame.pack(side=RIGHT, padx=20)

Search = StringVar()
search_entry = Entry(search_frame, textvariable=Search, width=20, bd=2,
                     font="arial 16")
search_entry.pack(side=LEFT, padx=10, pady=20)

def focus_search():
    search_entry.focus_set()

# ---------- IMAGES ----------
def load_image(path, size):
    try:
        img = Image.open(path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Image not found: {path}")
        return None

search_img = load_image(os.path.join(IMAGE_DIR, "search.png"), (30, 30))
layer_img = load_image(os.path.join(IMAGE_DIR, "layer.jpg"), (40, 40))

if search_img:
    Srch = Button(search_frame, text="Search", compound=LEFT, image=search_img,
                  bg='#68ddfa', font="arial 12 bold", padx=10,
                  command=focus_search)
    Srch.pack(side=LEFT, padx=5)

if layer_img:
    Update_button = Button(root, image=layer_img, bg="#c36464")
    Update_button.place(x=110, y=64)

# ---------- REGISTRATION NO. & DATE ----------
Label(root, text="Registration No", font="arial 13", fg=framebg, bg=background).place(x=30, y=150)
Label(root, text="Date", font="arial 13", fg=framebg, bg=background).place(x=500, y=150)

Registration = StringVar()
Date = StringVar()

reg_entry = Entry(root, textvariable=Registration, width=15, font="arial 10")
reg_entry.place(x=160, y=150)

today = date.today()
d1 = today.strftime("%d/%m/%Y")

date_entry = Entry(root, textvariable=Date, width=15, font="arial 10")
date_entry.place(x=550, y=150)
Date.set(d1)

# ---------- STUDENT DETAILS ----------
obj = LabelFrame(root, text="Student's Details", font=20, bd=2, width=900, bg=framebg, fg=framefg, height=250, relief=GROOVE)
obj.place(x=30, y=200)

Label(obj, text="Full Name:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=50)
Label(obj, text="Date of Birth:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=100)
Label(obj, text="Gender:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=150)
Label(obj, text="Class:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=50)
Label(obj, text="Religion:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=100)
Label(obj, text="Skills:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=150)


Name = StringVar()
name_entry = Entry(obj, textvariable=Name,width=20,font="arial 10")
name_entry.place(x=160,y = 50)


DOB = StringVar()
dob_entry = Entry(obj, textvariable=DOB,width=20,font="arial 10")
dob_entry.place(x=160,y = 100)

radio = IntVar()
R1= Radiobutton(obj,text="Male", variable=radio,value=1,bg=framebg, fg=framefg, command= selection)
R1.place(x=150, y = 150)

R2= Radiobutton(obj,text="Female", variable=radio,value=2,bg=framebg, fg=framefg, command= selection)
R2.place(x=200, y = 150)



Name = StringVar()
name_entry = Entry(obj, textvariable=Name,width=20,font="arial 10")
name_entry.place(x=160,y = 50)



Name = StringVar()
name_entry = Entry(obj, textvariable=Name,width=20,font="arial 10")
name_entry.place(x=160,y = 50)










# ---------- PARENT DETAILS ----------
obj2 = LabelFrame(root, text="Parent's Details", font=20, bd=2, width=900, bg=framebg, fg=framefg, height=220, relief=GROOVE)
obj2.place(x=30, y=470)

Label(obj2, text="Father's Name:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=30)
Label(obj2, text="Father's Occupation:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=80)
Label(obj2, text="Mother's Name:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=30)
Label(obj2, text="Mother's Occupation:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=80)

# ---------- MAIN LOOP ----------
root.mainloop()
