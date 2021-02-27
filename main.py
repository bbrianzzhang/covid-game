import random

commands = ['go to work', 'end day']
money = 10000
days = 0
covidChance = 20


def receive_input():
    global days
    possible_actions = ""
    for command in commands:
        possible_actions += command + " "
    print("Choose an action: " + possible_actions)
    while True:
        user_input = input("Choose an action")
        if user_input in commands:
            days += 1
            return user_input
        else:
            print("Not a valid action.")


def go_outside():
    global money
    x = random.randint(0, 100)
    if x < covidChance:
        print("While outside, you caught COVID. You recover, but the price is high.")
        money -= 5000


def get_groceries():
    print("You go outside to get groceries.")
    global money
    money -= 200
    go_outside()


def work():
    global money
    money += 600
    go_outside()


while True:
    dayOver = False
    print("Day " + str(days))
    print("You have " + str(money) + " money.")
    canWork = True
    while not dayOver:
        action = receive_input()
        if action == 'end day':
            dayOver = True
        elif action == 'go to work':
            if canWork:
                work()
                canWork = False
            else:
                print("You already went to work.")
    days += 1
    if days % 7 == 0:
        get_groceries()
