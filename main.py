import random

commands = ['go to work', 'end day']
money = 100000
days = 0
covidChanceGroceries = 20
covidChanceWork = 5
foodDelivery = False
government = True
investment = False


def receive_input():
    global days
    possible_actions = ""
    for command in commands:
        possible_actions += command + " "
    print("Choose an action: " + possible_actions)
    while True:
        user_input = input()
        if user_input in commands:
            return user_input
        else:
            print("Not a valid action.")


def check_conditions():
    global money, foodDelivery, days, investment
    if money > 15000 and foodDelivery == False:
        answer = input("You are given the opportunity to invest in a food delivery company. Would you like to invest $5000? ("
              "Y/N)")
        if answer == "Y":
            print("Money invested.")
            money -= 5000
            foodDelivery = True
    if money>20000 and investment == False:
        print("Your financial advisor offers you an opportunity to invest.")
        investment = True
    if days == 50:
        print("You are encouraged by a co-worker to run for government.")
        print("It costs $50000 to run.")
        commands.append("run for government")



def run_for_government():
    global money, government
    money -= 50000
    x = random.randint(1, 2)
    if x==1:
        print("Your campaign was not successful. You must try again another day.")
    else:
        print("Your campaign was successful! Congratulations.")
        print("You now have more options in your daily life.")
        government = True
        commands.append("create mask production facility")
        commands.append("create COVID testing center")
        commands.append("create vaccine research center")



def get_groceries():
    print("You go outside to get groceries.")
    global money
    money -= 200
    x = random.randint(0, 100)
    if foodDelivery:
        if input("Would you like to order your groceries instead? It will cost extra money but you have no chance of "
                 "getting COVID (Y/N)") == "Y":
            money -= 50
            print("You ordered groceries online.")
            return
        else:
            print("You chose to go out yourself.")

    if x < covidChanceGroceries:
        print("While outside, you caught COVID. You recover, but the price is high.")
        money -= 5000


def work():
    global money
    money += 600
    x = random.randint(0, 100)
    if x < covidChanceWork:
        print("While outside, you caught COVID. You recover, but the price is high.")
        money -= 5000


while True:
    dayOver = False
    print("Day " + str(days))
    print("You have " + str(money) + " money.")
    canWork = True
    check_conditions()
    while not dayOver:
        action = receive_input()
        if action == 'end day':
            dayOver = True
            days += 1
        elif action == 'go to work':
            if canWork:
                work()
                canWork = False
            else:
                print("You already went to work.")
        elif action == 'run for government':
            if money > 50000:
                run_for_government()
            else:
                print("You do not have enough money to run for government.")
    if days % 7 == 0:
        get_groceries()
