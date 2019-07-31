import SpaceMagic
import tkinter
from tkinter.filedialog import askopenfilename


##main
##background
root = tkinter.Tk()
# root.wm_iconbitmap('diagrams.ico')
# root.iconbitmap('diagrams.ico')root.wm_iconbitmap('diagrams.ico')
# root.iconbitmap('diagrams.ico')
root.title("Merge No More!")
root.configure(background="white")
root.geometry("730x165")

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
browsebutton1.pack()
pathlabel1 = tkinter.Label(root)
pathlabel1.pack()

#Colum selector button
# columselectorbutton1 = tkinter.Button(root, text="Select index of colum", width=50, command=)

#Browse button 2 +label
csv2 = ""
browsebutton2 = tkinter.Button(root, text="Add Comparison Spreadsheet", width=50, command=import_csv2_data)
browsebutton2.pack()
pathlabel2 = tkinter.Label(root)
pathlabel2.pack()

#Merge function call:
def merge(event):
    SpaceMagic.main(csv1, csv2)


#Merge button
mergebutton = tkinter.Button(root, text="Merge", width=50)
mergebutton.bind("<Button-1>", merge)
mergebutton.pack()


##exit function
def close_root():
    root.destroy()
    exit()


# #exit button
exitbutton = tkinter.Button(root, text="Exit", width=50, command=close_root)
exitbutton.pack()



#run the main loop
root.mainloop()