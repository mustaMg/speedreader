#%%
import tkinter as tk
import datetime
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

def counting():
    global number
    number += inc_val
    PN.config(text=number)
    PN.after(1000, counting)


root = tk.Tk()
root.geometry("400x200")
root.configure(bg='white')
root.rowconfigure([0, 1, 2, 3], minsize=50, weight=1)
root.columnconfigure([0, 1, 2], minsize=50, weight=1)
# to put some buttons exc we need to divide the panel into sections

btn_pause = tk.Button(master=root, text='||', command=pause)
btn_pause.grid(row=1, column=0)
btn_play = tk.Button(master=root, text='|>', command=play)
btn_play.grid(row=1, column=1)

number = 0
PN = tk.Label(master=root, text=number, width=36, height=20, font=('Times New Roman', 36))
PN.grid(row=0, column=1)

incc = tk.Button(master=root, text='>>', command=increase_inc)
incc.grid(row=1, column=2)

incc_L = tk.Label(master=root, text=inc_val)
incc_L.grid(row=2,column=2)

counting()

lab = tk.Label(root)
lab.grid(row=2, column=1) # empty
def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    root.title(time)
    lab.after(1000, clock) # run itself again after 1000 ms
    
# run first time
clock()

root.mainloop()

# saniyede 300 kelime gosterebilmek icin 1 saniyede 5 kelime gecmesi gerekiyor
#%%
