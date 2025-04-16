from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
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
root.title("Student Registration")
root.geometry("1250x700+210+100")
root.config(bg=background)

# ---------- EXCEL FILE CHECK ----------
file_path = 'student_data.xlsx'
file = pathlib.Path(file_path)

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

    wb.save(file_path)

# ---------- HEADER SECTION ----------
Label(root, text="Email: hudsonnbenhuraa@gmail.com", bg="#f0687c",
      anchor='e', fg='white', font='arial 12', height=2).pack(side=TOP, fill="x")

Label(root, text="STUDENT REGISTRATION SYSTEM", bg="#c36464", fg='white',
      font='arial 20 bold', height=2).pack(side=TOP, fill="x")

# ---------- SEARCH BOX ----------
Search = StringVar()
Entry(root, textvariable=Search, width=15, bd=2, font="arial 20").place(x=850, y=70)
# Label(root, text="Search", font="arial 12 bold", bg=background, fg="white").place(x=790, y=90)

# ---------- MAIN LOOP ----------
root.mainloop()
