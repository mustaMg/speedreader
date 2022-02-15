#%%
import tkinter as tk
import datetime
from tkinter.filedialog import askopenfilename
from  book_reader import *
# Label(root, text = "Hello World!", font= ('Helvetica 25 bold')).place(relx=.5, rely=.5,anchor= CENTER)

inc_val = 1

def pause():
    global inc_val
    inc_val = 0 

def play():
    global inc_val
    inc_val = 1
    incc_L['text'] = inc_val

def increase_inc():
    global inc_val
    inc_val += 9
    incc_L['text'] = inc_val

def inc_wpm():
    global wpm
    wpm += 10
    lbl_wpm['text'] = wpm

def dec_wpm():
    global wpm
    wpm -= 10
    lbl_wpm['text'] = wpm

def counting():
    global number
    number += inc_val
    PN.config(text=number)
    PN.after(1000, counting)

def reset():
    global ind
    ind = 0

reading = False
ind = 0
wpm = 150
def list_pointer():
    global ind
    global wpm
    if reading is True:
        ind +=1 
    new = dd[ind]
    text.config(text=new)
    text.after(int(60000/wpm), list_pointer)

def ch_reading():
    global reading
    if reading is False:
        reading = True
    elif reading is True:
        reading = False
    return reading

root = tk.Tk()
root.rowconfigure([0,1,2], minsize=1, weight=1)
root.columnconfigure([0,1,2], minsize=1, weight=1)

fr_buttons = tk.Frame(root)
btn_open = tk.Button(fr_buttons, text="Open")
btn_save = tk.Button(fr_buttons, text="Save As...")
# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=0, column=1, sticky="ew")
# fr_buttons.grid(row=0, column=0, sticky="ns")
fr_play = tk.Frame(root)
btn_pause = tk.Button(fr_play, text='||', command=pause)
btn_play = tk.Button(fr_play, text='|>', command=play)
incc = tk.Button(fr_play, text='>>', command=increase_inc)
# btn_pause.grid(row=0, column=0)
# btn_play.grid(row=0,column=1)
# incc.grid(row=0, column=2)
# fr_play.grid(row=1, column=0, sticky='ns')

number = 0
PN = tk.Label(master=root, text=number, font=(12))
# PN.grid(row=2, column=1)
incc_L = tk.Label(master=root, text=inc_val)
# incc_L.grid(row=2,column=2)

counting()

dd = ['a', 'b', 'c', 'd', 'e', 'a1', 'b1', 'c1', 'd1', 'e1', 'a2', 'b2', 'c2', 'd2', 'e2', 'a3', 'b3', 'c3', 'd3', 'e3', 'a4', 'b4', 'c4', 'd4', 'e4', 'a5', 'b5', 'c5', 'd5', 'e5'\
    'a', 'b', 'c', 'd', 'e', 'a1', 'b1', 'c1', 'd1', 'e1', 'a2', 'b2', 'c2', 'd2', 'e2', 'a3', 'b3', 'c3', 'd3', 'e3', 'a4', 'b4', 'c4', 'd4', 'e4', 'a5', 'b5', 'c5', 'd5', 'e5'\
        'a', 'b', 'c', 'd', 'e', 'a1', 'b1', 'c1', 'd1', 'e1', 'a2', 'b2', 'c2', 'd2', 'e2', 'a3', 'b3', 'c3', 'd3', 'e3', 'a4', 'b4', 'c4', 'd4', 'e4', 'a5', 'b5', 'c5', 'd5', 'e5'\
            'a', 'b', 'c', 'd', 'e', 'a1', 'b1', 'c1', 'd1', 'e1', 'a2', 'b2', 'c2', 'd2', 'e2', 'a3', 'b3', 'c3', 'd3', 'e3', 'a4', 'b4', 'c4', 'd4', 'e4', 'a5', 'b5', 'c5', 'd5', 'e5']
text = tk.Label(master=root, text='not started')
text.grid(row=0 , column=1)

fr_book = tk.Frame(root)
btn_start = tk.Button(fr_book, text='|>', command=ch_reading)
btn_stop = tk.Button(fr_book,  text='||', command=ch_reading)

fr_book.grid(row=1, column=1)
btn_stop.grid(row=0, column=1)
btn_start.grid(row=0, column=2)



fr_wpm = tk.Frame(root)
btn_inc_wpm = tk.Button(fr_wpm, text="+", command=inc_wpm)
lbl_wpm = tk.Label(fr_wpm, text=wpm)
btn_dec_wpm = tk.Button(fr_wpm, text='-', command=dec_wpm)
btn_rst = tk.Button(fr_wpm, text='R',command=reset())
fr_wpm.grid(row=2, column=1)

btn_inc_wpm.grid(row=0, column=2)
lbl_wpm.grid(row=1,column=2)
btn_dec_wpm.grid(row=2, column=2)
btn_rst.grid(row=3, column=2)


list_pointer()

def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    root.title(time)
    root.after(1000, clock) # run itself again after 1000 ms
    
clock()

root.mainloop()
#%%
