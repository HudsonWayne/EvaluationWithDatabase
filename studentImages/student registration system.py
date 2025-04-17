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

# ---------- EMAIL BAR AT THE TOP ----------
Label(root, text="Email: hudsonnbenhuraa@gmail.com", bg="#f0687c",
      anchor='e', fg='white', font='arial 12', height=2).pack(side=TOP, fill="x")

# ---------- HEADER SECTION WITH SEARCH ----------
header_frame = Frame(root, bg="#c36464", height=80)
header_frame.pack(side=TOP, fill="x")

title_frame = Frame(header_frame, bg="#c36464")
title_frame.pack(side=LEFT, padx=20)

Label(title_frame, text="STUDENT REGISTRATION", bg="#c36464", fg='white',
      font='arial 20 bold', height=2).pack()

search_frame = Frame(header_frame, bg="#c36464")
search_frame.pack(side=RIGHT, padx=20)

Search = StringVar()
search_entry = Entry(search_frame, textvariable=Search, width=20, bd=2,
                     font="arial 16")
search_entry.pack(side=LEFT, padx=10, pady=20)

# Function to focus on the search bar when the button is clicked
def focus_search():
    search_entry.focus_set()

# Search Button with icon
search_img_path = "images/search.png"
if os.path.exists(search_img_path):
    search_img = Image.open(search_img_path)
    search_img = search_img.resize((30, 30))
    imageicon3 = ImageTk.PhotoImage(search_img)

    Srch = Button(search_frame, text="Search", compound=LEFT, image=imageicon3,
                  bg='#68ddfa', font="arial 12 bold", padx=10,
                  command=focus_search)
    Srch.pack(side=LEFT, padx=5)
else:
    print("Image not found:", search_img_path)

# ---------- MAIN LOOP ----------
root.mainloop()
