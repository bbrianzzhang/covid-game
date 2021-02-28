from tkinter import *
import threading
import time

def game_loop():
    while True:
        time.sleep(0.03)
        print(time_tracker.get())
        if time_tracker.get() == 8:
            x.set(1)
            word.set("You missed a call while you were at work. 510-029-4391 left a voicemail asking you to call back...")
            type_effect()
            time_tracker.set(9)
            call_number.grid(row=9, column=1,sticky="ew")
            call_field.grid(row=9, column=2,sticky=W)

def time_increment():
    while True:
        time.sleep(1)
        time_tracker.set(time_tracker.get()+1)

def type_effect():
    message.config(text=word.get()[:x.get()],anchor='nw')
    if x.get() < len(word.get()):
        threading.Timer(0.025, type_effect).start()
        x.set(x.get()+1)
        if x.get() == len(word.get()) - 1 and go_work.winfo_ismapped() == False:
            go_work.grid(row=8, column=1,sticky="ew")

def work():
    go_work["state"] = DISABLED
    if frame_stats.winfo_ismapped() == False:
        frame_stats.grid(row=3, column=4,sticky="n")
        money_label = Label(frame_stats, text="money:")
        money_label.grid(row=0, column=1)
    # import brians code
    threading.Timer(3, enable_work).start()

def enable_work():
    go_work["state"] = NORMAL

def call():
    return

root = Tk()
root.title("note taker")
root.geometry("900x200")
word = StringVar(root, "The pandemic hits… Your office job is one of the few unaffected. You're content as you continue to go to work…")

time_tracker = IntVar(root, value=0)
x = IntVar(root, value=1)

thread_time = threading.Thread(target=time_increment)
thread_time.start()
thread_loop = threading.Thread(target=game_loop)
thread_loop.start()

intro = Label(root, text="COVID adventure game...", width=100,pady=10)
intro.grid(row=0, column=0, columnspan=8)

go_work = Button(root, text="go to work...", anchor="w", command=work)
call_number = Button(root, text="call number", anchor="w",command=call)
call_field = Entry(root, width=10)

message = Label(root, text="", width=40 , wraplength=300, anchor='nw',pady=5,justify=LEFT)
message.grid(row=3, column=1, columnspan=2, sticky=W)

label_filler = Label(root,text=" ")
label_filler.grid(column=0,row=0,rowspan=3)
frame_stats = LabelFrame(root, text="resources...",padx=5,pady=5)

type_effect()

root.mainloop()
