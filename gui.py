from tkinter import *
import threading
import time
import random

def game_loop():
    while True:
        time.sleep(0.03)
        if frame_stats.winfo_ismapped():
            update_resources()
        if time_tracker.get() == 15:
            x.set(0)
            word.set("You missed a call while you were at work. 510-029-4391 left a voicemail asking you to call back...")
            while currently_typing.get():
                print("")
            type_effect("call")
            time_tracker.set(16)
        if time_tracker.get() > 25 and time_tracker.get()%50 == 0 and key_actions["call_0"] == False:
            while currently_typing.get():
                print("")
            x.set(0)
            word.set("You missed a call while you were at work. 510-029-4391 left a voicemail asking you to call back...")
            type_effect("none")
        if unlocked_dict["food"] == True and resources_dict["food"] == 1:
            resources_dict["food"] = 0
            while currently_typing.get():
                print("currentlytying",currently_typing.get())
            x.set(0)
            word.set("Your pantry ran out. Soon you will succumb to hunger if you don't refill...")
            type_effect("n")
        if resources_dict["food"] < -2:
            print("player died")
        if time_tracker.get() > 60 and key_actions["call_0"] == True and random.randint(1,1000) == 1 and currently_typing.get() == False and key_actions["call_1"] == False:
            while currently_typing.get():
                None
            x.set(0)
            word.set("Hey. I'm Andy from BuberEats, a startup for food delivery. We want to help deliver you food safely. If you're interested in our service, call me back at 510-291-2222 and you can use our service after a $100 deposit.")
            type_effect("n")
        if time_tracker.get() > 90 and key_actions["call_1"] == True and key_actions["call_0"] == True and random.randint(1,1000) == 1 and key_actions["call_2"] == False:
            while currently_typing.get():
                None
            x.set(0)
            word.set("This newest machine model will help you do your job! Call 1-800-696-3929 today to get your model for only $250.")
            type_effect("n")
        if time_tracker.get() == 300:
            time_tracker.set(301)
            while currently_typing.get():
                print("")
            x.set(0)
            word.set(
                "As the pandemic worsens,  you begin to feel more and more worried about the crisis. You start paying more attention to the news and keeping up with the COVID statistic websites.")
            type_effect("n")
            unlocked_dict["deaths"] = True

        # if random.randint(0, 10000) == 1 and key_actions["call_1"] == False:
        #     while currently_typing.get():
        #         print("")
        #     x.set(0)
        #     word.set("You missed a call while you were at work. 510-298-2911 left a voicemail asking you to call back...")
        #     type_effect("n")

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
                    food_label.config(text="food: plenty")
                elif resources_dict["food"] > 5:
                    food_label.config(text="food: enough")
                elif resources_dict["food"] > 3:
                    food_label.config(text="food: a bit")
                elif resources_dict["food"] > 0:
                    food_label.config(text="food: low")
            if key == "deaths":
                death_label.grid(row=0, column=0)
                new_stat = "COVID deaths: " + str(resources_dict["deaths"])
                death_label.config(text=new_stat)

def time_increment():
    while True:
        time.sleep(1)
        if key_actions["passive_income"]:
            resources_dict["money"] += 10
        time_tracker.set(time_tracker.get()+1)
        if time_tracker.get()%3==0 and unlocked_dict["food"]:
            print(resources_dict["food"])
            resources_dict["food"]-=1
        if time_tracker.get()%6==0 and unlocked_dict["deaths"]:
            resources_dict["deaths"] += random.randint(time_tracker.get()//2, time_tracker.get())

def type_effect(place_something):
    if x.get() == 0:
        currently_typing.set(True)
    message.config(text=word.get()[:x.get()],anchor='nw')
    if x.get() < len(word.get()):
        threading.Timer(0.05, type_effect, [place_something]).start()
        x.set(x.get()+1)
        if x.get() == len(word.get()) - 1:
            currently_typing.set(False)
            time.sleep(.5)
            if go_work.winfo_ismapped() == False:
                unlocked_dict["money"] = True
                go_work.place(x=20, y=130, width=150)
                frame_stats.place(x=400, y=40)
                frame_covid_stats.place(x=600, y=40)
            if call_number.winfo_ismapped() == False and place_something == "call":
                call_number.place(x=20, y=160, width=150)
                call_field.place(x=180, y=160, width=150)
            if place_something == "call_0":
                x.set(0)
                word.set("Hello? God, you finally picked up. It's nuts out there, huh? Nobody knows what to expect anymore. Just look out for yourself and try not to go out too much... You might get it just from a trip to the grocers.")
                type_effect('done call 0')
                unlocked_dict["food"] = True
            if place_something == "call_1":
                x.set(0)
                if resources_dict["money"] >= 100:
                    resources_dict["money"] -= 100
                    word.set("Hey! Glad to hear that you're interested in us! You won't regret your investment. Our delivery portions are big, and will last you for a bit.")
                    order_food.place(x=20, y=220, width=150)
                else:
                    word.set("sorry dawg we dont fuck with broke bros")
                type_effect('none')
            if place_something == "call_2":
                x.set(0)
                if resources_dict["money"] >= 250:
                    resources_dict["money"] -= 250
                    key_actions["passive_income"] = True
                    word.set("Now any tedious office work is completed effortlessly.")
                else:
                    word.set("Can't pay? Get lost!")
                type_effect("none")
            if place_something == "contacted":
                x.set(0)
                word.set("You've already contacted us and made a sweet deal!")
                type_effect('n')
            if place_something == "done call 0":
                get_food_button.place(x=20, y=190, width=150)
            if place_something == "bad call":
                x.set(0)
                word.set("Your call didn't go through. Are you sure you called the right number? Or maybe they're busy...")
                type_effect('none')

def catch_covid(chance):
    random_num = random.randint(0, 100)
    if random_num < chance:
        while currently_typing.get():
            True
        x.set(0)
        word.set("You test positive for COVID-19. The doctor tells you to stay home, but you know money can save your life.")
        if resources_dict["money"] > 1000:
            resources_dict["money"] -= 1000
        else:
            resources_dict["money"] = 0
        type_effect("none")

def work():
    go_work["state"] = DISABLED
    resources_dict["money"] += 20
    threading.Timer(3, enable_work).start()
    catch_covid(1)

def enable_work():
    go_work["state"] = NORMAL

def call():
    if len(call_field.get()) != 0:
        input_number = call_field.get()
        call_number["state"] = DISABLED
        threading.Timer(5, enable_call).start()
        x.set(0)
        word.set("Calling....................")
        input_number_num = ""
        for i in input_number:
            if i in "0123456789":
                input_number_num += i
        if input_number_num == "5100294391":
            key_actions["call_0"] = True
            type_effect("call_0")
        elif input_number_num == "5102912222":
            if key_actions["call_1"]:
                type_effect("contacted")
            else:
                key_actions["call_1"] = True
                type_effect("call_1")
        elif input_number_num == "18006963929":
            if key_actions["call_2"]:
                type_effect("contacted")
            else:
                key_actions["call_2"] = True
                type_effect("call_2")
        else:
            type_effect("bad call")
    else:
        x.set(0)
        word.set("You cannot call an empty number...")
        type_effect("none")

def enable_call():
    call_number["state"] = NORMAL

def get_food():
    catch_covid(5)
    resources_dict["food"] = 10
    if resources_dict["money"] >= 5:
        resources_dict["money"] -= 5

def order():
    resources_dict["food"] = 125
    if resources_dict["money"] >= 50:
        resources_dict["money"] -= 50

root = Tk()
root.title("COVID Adventure Game")
root.geometry("960x540")
word = StringVar(root, "The pandemic hits… Your office job is one of the few unaffected. You're content as you continue to go to work…")

resources_dict = {
    "money": 0,
    "food": 10,
    "deaths": 50,
}

unlocked_dict = {
    "money": False,
    "food": False,
    "deaths": False,
}


key_actions = {
    "call_0": False,
    "call_1": False,
    "call_2": False,
    "passive_income": False
}

currently_typing = BooleanVar(root, False)
time_tracker = IntVar(root, value=0)
x = IntVar(root, value=1)

# start game loop
thread_time = threading.Thread(target=time_increment)
thread_time.start()
thread_loop = threading.Thread(target=game_loop)
thread_loop.start()

# add frame

# buttons n shit
go_work = Button(root, text="go to work",  command=work)
call_number = Button(root, text="call number", command=call)
call_field = Entry(root, width=10)
get_food_button = Button(root, text="buy food", command=get_food)
order_food = Button(root, text="order food", command=order)

frame_stats = LabelFrame(root, text="resources...",padx=5,pady=5)
frame_covid_stats = LabelFrame(root, text="COVID stats", padx=5, pady=15)

#COVID stat labels
death_label = Label(frame_covid_stats, text="deaths: 30")
hospital_capacity_label = Label(frame_covid_stats, text="hospital capacity: 90% full")

# resource labels
money_label = Label(frame_stats, text="money: 0")
food_label = Label(frame_stats, text="food: 10")

# where messages go
message = Label(root, text="", wraplength=300 ,justify=LEFT)
message.place(x=20, y=40, height=85, width=350)

type_effect("none")

root.mainloop()
