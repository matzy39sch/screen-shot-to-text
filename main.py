# import the GUI manager package
import tkinter
from typing import Sized
from tkinter import *
import screenshot_to_text

def image_to_text():
    start_x_value = int(my_text_box_start_x.get())
    start_y_value = int(my_text_box_start_y.get())
    end_x_value = int(my_text_box_end_x.get())
    end_y_value = int(my_text_box_end_y.get())
    text = screenshot_to_text.image_to_text(start_x_value, start_y_value, end_x_value, end_y_value)
    log.insert(1.0, text)
    return text

start_x_value = 0
start_y_value = 0
end_x_value = 0
end_y_value = 0

my_root_window = tkinter.Tk()

start_x = tkinter.IntVar(value=900)
start_y = tkinter.IntVar(value=200)
end_x = tkinter.IntVar(value=1200)
end_y = tkinter.IntVar(value=400)

frame_start_x = tkinter.Frame(my_root_window)
label_dir_start_x =Label(frame_start_x, text="Start X", height=4).pack(side=LEFT)

my_text_box_start_x = Entry(frame_start_x, textvariable= start_x, width=5)
my_text_box_start_x.pack(side=LEFT)
frame_start_x.grid(row=0, column=0, sticky=W)

frame_start_y = tkinter.Frame(my_root_window)
label_dir_start_y =Label(frame_start_y, text="Start Y", height=4).grid(row=1, column=0)
my_text_box_start_y=Entry(frame_start_y, textvariable=start_y, width=5)
my_text_box_start_y.grid(row=1, column=1)
frame_start_y.grid(row=1, column=0, sticky=W)

frame_end_x = tkinter.Frame(my_root_window)
label_dir_end_x =Label(frame_end_x, text="END X", height=4).grid(row=2, column=0)
my_text_box_end_x = Entry(frame_end_x, textvariable= end_x,width=5)
my_text_box_end_x.grid(row=2, column=1)
frame_end_x.grid(row=2, column=0, sticky=W)


frame_end_y = tkinter.Frame(my_root_window)
label_dir_end_y =Label(frame_end_y, text="END Y", height=4).grid(row=3, column=0)
my_text_box_end_y=Entry(frame_end_y, textvariable= end_y,width=5)
my_text_box_end_y.grid(row=3, column=1)
frame_end_y.grid(row=3, column=0, sticky=W)


frame = tkinter.Frame(my_root_window)
scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
log = tkinter.Text(frame, width=40)
# log.config(state=tkinter.DISABLED)
log.pack(expand=1)
scrollbar.config(command=log.yview)
frame.grid(row=4, column=0)


HEIGHT = 100
WIDTH = 400
canvas = tkinter.Canvas(my_root_window, height = HEIGHT, width=WIDTH)


message = tkinter.StringVar()
message.set('Press F12 or the Press Me! button \n to grab screenshot of the given coordinates \n then convert it to text!')
label = tkinter.Label(my_root_window, text="", textvariable=message, font='size, 12')
button = tkinter.Button( my_root_window, text='Press Me!', command=image_to_text )

label.grid()
button.grid()
canvas.grid()

my_root_window.bind("<Escape>",  lambda q: my_root_window.quit() )
my_root_window.bind("<F12>",  lambda e: image_to_text())
my_root_window.wm_title("Screenshot to text")
button.focus()

my_root_window.mainloop()