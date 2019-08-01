import SpaceMagic
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter import *

##main
##background
root = tkinter.Tk()
root.title("Merge No More!")
root.configure(background="white")
root.geometry("490x250")

##file browsers
def import_csv1_data():
    global csv1
    csv_file_path = askopenfilename()
    print(csv_file_path)
    pathlabel1.config(text=csv_file_path)
    csv1 = (csv_file_path)

def import_csv2_data():
    global csv2
    csv_file_path = askopenfilename()
    print(csv_file_path)
    pathlabel2.config(text=csv_file_path)
    csv2 = (csv_file_path)


#Browse button 1 +label
csv1 = ""
browsebutton1 = tkinter.Button(root, text="Add Base Spreadsheet",  width=50, command=import_csv1_data)
browsebutton1.place(x= 0, y = 0)
pathlabel1 = tkinter.Label(root)
pathlabel1.place(x= 0, y = 30)

def get_col1_input(event):
    global col1
    col1 = col_1.get()
    print(col1)
    return col1

def get_col2_input(event):
    global col2
    col2 = col_2.get()
    print(col2)
    return col2

#Colum selector button
columselectorbutton1 = tkinter.Button(root, text="Select index of colum", width=15)
columselectorbutton1.bind("<Button-1>", get_col1_input)
columselectorbutton1.place(x = 320, y = 57.25)
tkinter.Label(root, text="Add colum number:").place(x= 0, y = 150)
tkinter.Label(root, text="Add colum number:").place(x= 0, y = 60)
col_1 = tkinter.Entry(root)
col_1.place(x= 130, y = 58)


#Browse button 2 +label
csv2 = ""
browsebutton2 = tkinter.Button(root, text="Add Comparison Spreadsheet", width=50, command=import_csv2_data)
browsebutton2.place(x= 0, y = 90)
pathlabel2 = tkinter.Label(root)
pathlabel2.place(x= 0, y = 120)


#Colum selector button
columselectorbutton2 = tkinter.Button(root, text="Select index of colum", width=15)
tkinter.Label(root, text="Add colum number:").place(x= 0, y = 150)
columselectorbutton2.bind("<Button-1>", get_col2_input)
columselectorbutton2.place(x = 320, y = 147.25)
tkinter.Label(root, text="Add colum number:").place(x= 130, y = 147)
col_2 = tkinter.Entry(root)
col_2.place(x= 130, y = 147)

#Merge function call:
def merge(event):
    SpaceMagic.main(csv1, csv2, col1, col2)


#Merge button
mergebutton = tkinter.Button(root, text="Merge", width=50)
mergebutton.bind("<Button-1>", merge)
mergebutton.place(x= 0, y = 180)


##exit function
def close_root():
    root.destroy()
    exit()


# #exit button
exitbutton = tkinter.Button(root, text="Exit", width=50, command=close_root)
exitbutton.place(x= 0, y = 210)


#run the main loop
root.mainloop()