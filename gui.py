from tkinter import *
import threading
import time

def game_loop():
    while True:
        time.sleep(0.03)
        if frame_stats.winfo_ismapped():
            update_resources()
        if time_tracker.get() == 15:
            x.set(1)
            word.set("You missed a call while you were at work. 510-029-4391 left a voicemail asking you to call back...")
            type_effect("call")
            time_tracker.set(16)

def update_resources():
    for key in resources_dict:
        if unlocked_dict[key]:
            if key == "money":
                money_label.grid(row=0, column=0)
                together = key + ": " + str(resources_dict[key])
                money_label.config(text=together)

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
                unlocked_dict["money"] = True
                go_work.place(x=20, y=100, width=100)
            if call_number.winfo_ismapped() == False and place_something == "call":
                call_number.place(x=20, y=130, width=100)
                call_field.place(x=130, y=130)
            if place_something == "call_0":
                x.set(1)
                word.set("Hello? God, you finally picked up.")
                type_effect('none')
            if place_something == "bad call":
                x.set(1)
                word.set("Your call didn't go through. Are you sure you called the right number? Or maybe they're busy...")
                type_effect('none')

def work():
    go_work["state"] = DISABLED
    if frame_stats.winfo_ismapped() == False:
        print("hm")
        frame_stats.place(x=400, y=40)

    resources_dict["money"] += 20
    threading.Timer(3, enable_work).start()

def enable_work():
    go_work["state"] = NORMAL

def call():
    if len(call_field.get()) != 0:
        input_number = call_field.get()
        call_number["state"] = DISABLED
        threading.Timer(5, enable_call).start()
        x.set(1)
        word.set("Calling....................")
        input_number_num = ""
        for i in input_number:
            if i in "0123456789":
                input_number_num += i
        if input_number_num == "5100294391":
            type_effect("call_0")
        elif input_number_num == "another num":
            True
            # called another call_number
        else:
            type_effect("bad call")
    else:
        x.set(1)
        word.set("You cannot call an empty number...")
        type_effect("none")

def enable_call():
    call_number["state"] = NORMAL

root = Tk()
root.title("COVID Adventure Game")
root.geometry("960x540")
word = StringVar(root, "The pandemic hits… Your office job is one of the few unaffected. You're content as you continue to go to work…")

resources_dict = {
    "money": 0
}

unlocked_dict = {
    "money": False
}

time_tracker = IntVar(root, value=0)
x = IntVar(root, value=1)

# start game loop
thread_time = threading.Thread(target=time_increment)
thread_time.start()
thread_loop = threading.Thread(target=game_loop)
thread_loop.start()

# add frame

# buttons n shit
go_work = Button(root, text="go to work...",  command=work)
call_number = Button(root, text="call number", command=call)
call_field = Entry(root, width=10)

frame_stats = LabelFrame(root, text="resources...",padx=5,pady=5)

# resource labels
money_label = Label(frame_stats, text="money: 0")


# where messages go
message = Label(root, text="", wraplength=300 ,justify=LEFT)
message.place(x=20, y=40, height=60, width=350)

type_effect("none")

root.mainloop()
