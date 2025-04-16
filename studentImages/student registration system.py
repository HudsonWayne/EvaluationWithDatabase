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

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"


root = Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=background)


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
    
Label(root,text="Email: hudsonnbenhuraa@gmail.com",width=10,height=3,bg="#f0687c",anchor='e').pack(side=TOP,fill="x")
Label(root,text="STUDENT REGISTRATION: hudsonnbenhuraa@gmail.com",width=10,height=2,bg="#c36464",fg='#fff',font= 'arial 20 bold').pack(side=TOP,fill="x")

    
    
    

root.mainloop()
