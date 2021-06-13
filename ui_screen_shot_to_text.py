import tkinter
from typing import Sized
from tkinter import *
from PIL import Image, ImageTk
import screenshot_to_text
from tkinter.filedialog import askopenfilename
import google_sheet

filename = ""

def update_image():
    img = Image.open(r"Capture.png")
    img = img.resize((200,200), Image.ANTIALIAS)
    photoImg =  ImageTk.PhotoImage(img)
    canvas.create_image((0, 0), anchor=NW ,image=photoImg, state="normal")
    canvas.theimage = photoImg

def image_to_text():
    start_x_value = int(my_text_box_start_x.get())
    start_y_value = int(my_text_box_start_y.get())
    end_x_value = int(my_text_box_end_x.get())
    end_y_value = int(my_text_box_end_y.get())
    text = screenshot_to_text.image_to_text(start_x_value, start_y_value, end_x_value, end_y_value)
    log.insert(1.0, text)
    sheet_name = url.get()
    if filename == '' and sheet_name != '':
        open_file()
    elif sheet_name != '':
        google_sheet.write_to_sheet(filename, text, sheet_name, 0, (2, 2))
    update_image()
    return text

def open_file():
    global filename
    filename = askopenfilename() 

my_root_window = tkinter.Tk()

# create inputs 
start_x = tkinter.IntVar(value=900)
start_y = tkinter.IntVar(value=200)
end_x = tkinter.IntVar(value=1200)
end_y = tkinter.IntVar(value=400)

frame_start_x = tkinter.Frame(my_root_window)
Label(frame_start_x, text="Start X", height=4).pack(side=LEFT)
my_text_box_start_x = Entry(frame_start_x, textvariable= start_x, width=5)
my_text_box_start_x.pack(side=LEFT)
frame_start_x.grid(row=0, column=0, sticky=W)

frame_start_y = tkinter.Frame(my_root_window)
Label(frame_start_y, text="Start Y", height=4).grid(row=1, column=0)
my_text_box_start_y=Entry(frame_start_y, textvariable=start_y, width=5)
my_text_box_start_y.grid(row=1, column=1)
frame_start_y.grid(row=1, column=0, sticky=W)

frame_end_x = tkinter.Frame(my_root_window)
Label(frame_end_x, text="END X", height=4).grid(row=2, column=0)
my_text_box_end_x = Entry(frame_end_x, textvariable= end_x,width=5)
my_text_box_end_x.grid(row=2, column=1)
frame_end_x.grid(row=2, column=0, sticky=W)

frame_end_y = tkinter.Frame(my_root_window)
Label(frame_end_y, text="END Y", height=4).grid(row=3, column=0)
my_text_box_end_y=Entry(frame_end_y, textvariable= end_y,width=5)
my_text_box_end_y.grid(row=3, column=1)
frame_end_y.grid(row=3, column=0, sticky=W)

url = tkinter.StringVar(value="")
frame_sheets = tkinter.Frame(my_root_window)
Label(frame_sheets, text="Google sheet name: ", height=4).grid(row=4, column=0)
url=Entry(frame_sheets, textvariable= url,width=50)
url.grid(row=4, column=1)
button = tkinter.Button( my_root_window, text='Browse', command=open_file )
button.grid(row=4, column=2)
frame_sheets.grid(row=4, column=0, sticky=W)

# create textarea
frame = tkinter.Frame(my_root_window)
scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
log = tkinter.Text(frame, width=40)
log.pack(expand=1)
scrollbar.config(command=log.yview)
frame.grid(row=5, column=0)

# create canvas
canvas = tkinter.Canvas(my_root_window, height = 200, width=200)
canvas.grid(row=1, column=3, rowspan=3)

# create Label
message = tkinter.StringVar()
message.set('Press F12 or the Press Me! button \n to grab screenshot of the given coordinates \n then convert it to text!')
label = tkinter.Label(my_root_window, text="", textvariable=message, font='size, 12')
label.grid()

# create button
button = tkinter.Button( my_root_window, text='Press Me!', command=image_to_text )
button.grid()
button.focus()

# bind keyboard commands
my_root_window.bind("<Escape>",  lambda q: my_root_window.quit() )
my_root_window.bind("<F12>",  lambda e: image_to_text())
my_root_window.wm_title("Screenshot to text")

my_root_window.mainloop()