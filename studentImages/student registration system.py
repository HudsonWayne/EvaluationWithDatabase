from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os

from tkinter.ttk import Combobox
import openpyxl,xlrd
from openpyxl import workbook
import pathlib


background = "#06283D"
framebg="#EDEDED"
framebg="#06283D"

root = Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=background)

root.mainloop()