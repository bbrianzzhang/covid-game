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
            type_effect("call")
            time_tracker.set(9)

def time_increment():
    while True:
        time.sleep(1)
        time_tracker.set(time_tracker.get()+1)

def type_effect(place_something):
    message.config(text=word.get()[:x.get()],anchor='nw')
    if x.get() < len(word.get()):
        threading.Timer(0.05, type_effect, [place_something]).start()
        x.set(x.get()+1)
        if x.get() == len(word.get()) - 1:
            time.sleep(.5)
            if go_work.winfo_ismapped() == False:
                go_work.place(x=20, y=100, width=100)
            if call_number.winfo_ismapped() == False and place_something == "call":
                call_number.place(x=20, y=130, width=100)
                call_field.place(x=130, y=130)

def work():
    go_work["state"] = DISABLED
    if frame_stats.winfo_ismapped() == False:
        frame_stats.place(x=350, y=40)
        money_label = Label(frame_stats, text="money:")
        money_label.grid(row=0, column=0)
    # import brians code
    threading.Timer(3, enable_work).start()

def enable_work():
    go_work["state"] = NORMAL

def call():
    return

root = Tk()
root.title("COVID Adventure Game")
root.geometry("960x540")
word = StringVar(root, "The pandemic hits… Your office job is one of the few unaffected. You're content as you continue to go to work…")

time_tracker = IntVar(root, value=0)
x = IntVar(root, value=1)

thread_time = threading.Thread(target=time_increment)
thread_time.start()
thread_loop = threading.Thread(target=game_loop)
thread_loop.start()


go_work = Button(root, text="go to work...",  command=work)
call_number = Button(root, text="call number", command=call)
call_field = Entry(root, width=10)

message = Label(root, text="", wraplength=300 ,justify=LEFT)
message.place(x=20, y=40, height=60, width=350)

frame_stats = LabelFrame(root, text="resources...",padx=5,pady=5)

type_effect("none")

root.mainloop()
