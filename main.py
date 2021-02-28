import random

commands = ['go to work', 'end day']
gameResources = {
    "money": 10000,
    "days": 0,
    "scientists": 0,
    "research": 0,
}
gameState = {
    "food_delivery": False,
    "government": False,
    "investment": False,
}
covidChanceGroceries = 20
covidChanceWork = 5


def receive_input():
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
    if gameResources["money"] > 15000 and not gameState["food_delivery"]:
        answer = input(
            "You are given the opportunity to invest in a food delivery company. Would you like to invest $5000? ("
            "Y/N)")
        if answer == "Y":
            print("Money invested.")
            gameResources["money"] -= 5000
            gameState["food_delivery"] = True
    if gameResources["money"] > 20000 and not gameState["investment"]:
        print("Your financial advisor offers you an opportunity to invest.")
        gameState["investment"] = True
    if gameResources["days"] == 50:
        print("You are encouraged by a co-worker to run for government.")
        print("It costs $50000 to run.")
        commands.append("run for government")


def run_for_government():
    gameResources["money"] -= 50000
    x = random.randint(1, 2)
    if x == 1:
        print("Your campaign was not successful. You must try again another day.")
    else:
        print("Your campaign was successful! Congratulations.")
        print("You now have more options in your daily life.")
        gameState["government"] = True
        commands.append("create mask production facility")
        commands.append("create COVID testing center")
        commands.append("create vaccine research center")


def get_groceries():
    print("You go outside to get groceries.")
    gameResources["money"] -= 200
    x = random.randint(0, 100)
    if gameState["food_delivery"]:
        if input("Would you like to order your groceries instead? It will cost extra money but you have no chance of "
                 "getting COVID (Y/N)") == "Y":
            gameResources["money"] -= 50
            print("You ordered groceries online.")
            return
        else:
            print("You chose to go out yourself.")

    if x < covidChanceGroceries:
        print("While outside, you caught COVID. You recover, but the price is high.")
        gameResources["money"] -= 5000


def work():
    gameResources["money"] += 600
    x = random.randint(0, 100)
    if x < covidChanceWork:
        print("While outside, you caught COVID. You recover, but the price is high.")
        gameResources["money"] -= 5000


while True:
    dayOver = False
    print("Day " + str(gameResources["days"]))
    print("You have " + str(gameResources["money"]) + " money.")
    canWork = True
    check_conditions()
    while not dayOver:
        action = receive_input()
        if action == 'end day':
            dayOver = True
            gameResources["days"] += 1
        elif action == 'go to work':
            if canWork:
                work()
                canWork = False
            else:
                print("You already went to work.")
        elif action == 'run for government':
            if gameResources["money"] > 50000:
                run_for_government()
            else:
                print("You do not have enough money to run for government.")
        elif action == 'hire scientist':
            if gameResources["money"] > 200:
                print("You have hired a scientist. They will help with COVID-related buildings")
                gameResources["scientists"] += 1
            else:
                print("You do not have enough money to hire a scientist")
        elif action == 'create vaccine research facility':
            if gameResources["money"] < 50000:
                print("You do not have enough money to build the vaccine research facility")
            elif gameResources["scientists"] < 10:
                print("You have not hired enough scientists to run the vaccine research facility")
            else:
                commands.append("research vaccines")
                commands.append("build vaccine distribution center")
                commands.remove("create vaccine research facility")
                gameResources["money"] -= 50000
                gameResources["scientists"] -= 10
        elif action == 'create mask production facility':
            if gameResources["money"] < 20000:
                print("You do not have enough money to build the mask production facility")
            elif gameResources["scientists"] < 10:
                print("You have not hired enough scientists to run the vaccine production facility")
            else:
                commands.append("create masks")
                commands.append("create mask distribution center")
                commands.remove("create mask production facility")
                gameResources["money"] -= 20000
                gameResources["scientists"] -= 10
        elif action == 'build COVID testing center':
            if gameResources["money"] < 30000:
                print("You do not have enough money to build the COVID testing center")
            elif gameResources["scientists"] < 10:
                print("You have not hired enough scientists to run the COVID testing center")
            else:
                commands.remove("build COVID testing center")
                gameResources["money"] -= 30000
                gameResources["scientists"] -= 10
                print("After building the COVID testing center, the chance of you catching COVID will go down "
                      "significantly as people will be more aware if they have the virus or not.")
                covidChanceGroceries = 5
                covidChanceWork = 1
    if gameResources["days"] % 7 == 0:
        get_groceries()
