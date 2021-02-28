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
        if time_tracker.get() > 25 and time_tracker.get()%50 == 0 and key_actions["call_0"] == False:
            while currently_typing:
                print("")
            x.set(1)
            word.set("You missed a call while you were at work. 510-029-4391 left a voicemail asking you to call back...")
            type_effect("none")
        if unlocked_dict["food"] == True and resources_dict["food"] == 1:
            resources_dict["food"] = 0
            while currently_typing:
                print("")
            x.set(1)
            word.set("Your pantry ran out. Soon you will succumb to hunger...")
            type_effect("n")
        if resources_dict["food"] < -2:
            print("player died")

def update_resources():
    for key in resources_dict:
        if unlocked_dict[key]:
            if key == "money":
                money_label.grid(row=0, column=0)
                together = key + ": " + str(resources_dict[key])
                money_label.config(text=together)
            if key == "food":
                food_label.grid(row=1, column=0)
                if resources_dict["food"] > 8:
                    food_label.config(text="food: full")
                elif resources_dict["food"] > 5:
                    food_label.config(text="food: enough")
                elif resources_dict["food"] > 3:
                    food_label.config(text="food: a bit")
                elif resources_dict["food"] > 0:
                    food_label.config(text="food: low")

def time_increment():
    while True:
        time.sleep(1)
        time_tracker.set(time_tracker.get()+1)
        if time_tracker.get()%3==0 and unlocked_dict["food"]:
            print(resources_dict["food"])
            resources_dict["food"]-=1

def type_effect(place_something):
    currently_typing = True
    message.config(text=word.get()[:x.get()],anchor='nw')
    if x.get() < len(word.get()):
        threading.Timer(0.05, type_effect, [place_something]).start()
        x.set(x.get()+1)
        if x.get() == len(word.get()) - 1:
            currently_typing = False
            time.sleep(.5)
            if go_work.winfo_ismapped() == False:
                unlocked_dict["money"] = True
                go_work.place(x=20, y=130, width=100)
                frame_stats.place(x=400, y=40)
            if call_number.winfo_ismapped() == False and place_something == "call":
                call_number.place(x=20, y=160, width=100)
                call_field.place(x=130, y=160)
            if place_something == "call_0":
                x.set(1)
                word.set("Hello? God, you finally picked up. It's nuts out there, huh? Nobody knows what to expect anymore. Just look out for yourself and try not to go out too much... You never know when you might get it.")
                type_effect('done call 0')
                unlocked_dict["food"] = True
            if place_something == "done call 0":
                get_food_button.place(x=20, y=190, width=100)
            if place_something == "bad call":
                x.set(1)
                word.set("Your call didn't go through. Are you sure you called the right number? Or maybe they're busy...")
                type_effect('none')

def work():
    go_work["state"] = DISABLED
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
            key_actions["call_0"] = True
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

def get_food():
    resources_dict["food"] = 10

root = Tk()
root.title("COVID Adventure Game")
root.geometry("960x540")
word = StringVar(root, "The pandemic hits… Your office job is one of the few unaffected. You're content as you continue to go to work…")

resources_dict = {
    "money": 0,
    "food": 10
}

unlocked_dict = {
    "money": False,
    "food": False
}

key_actions = {
    "call_0": False
}

currently_typing = False
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
get_food_button = Button(root, text="buy food", command=get_food)

frame_stats = LabelFrame(root, text="resources...",padx=5,pady=5)

# resource labels
money_label = Label(frame_stats, text="money: 0")
food_label = Label(frame_stats, text="food: 10")

# where messages go
message = Label(root, text="", wraplength=300 ,justify=LEFT)
message.place(x=20, y=40, height=85, width=350)

type_effect("none")

root.mainloop()
