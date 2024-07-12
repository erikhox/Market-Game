#These are all the big text boxes that I didn't want to see in my main file so i just put them here
def title():
    print("  __  __            _        _          _                 _       _             ")
    print(" |  \\/  |          | |      | |        (_)               | |     | |            ")
    print(" | \\  / | __ _ _ __| | _____| |_    ___ _ _ __ ___  _   _| | __ _| |_ ___  _ __ ")
    print(" | |\\/| |/ _` | '__| |/ / _ \\ __|  / __| | '_ ` _ \\| | | | |/ _` | __/ _ \\| '__|")
    print(" | |  | | (_| | |  |   <  __/ |_   \\__ \\ | | | | | | |_| | | (_| | || (_) | |   ")
    print(" |_|  |_|\\__,_|_|  |_|\\_\\___|\\__|  |___/_|_| |_| |_|\\__,_|_|\\__,_|\\__\\___/|_|   ")
    print("------------------------------------------------------------------------------\n")

def welcome():
    print("Welcome to the market simulator by Erik Hoxhaj.\n")
    print("Here you will be able to choose from a list of stocks, starting balance, and a starting year.")
    print("Then once started, you will be able to see the stock price, your current balance, and relevant news for the month if any.")
    print("Your goal is to follow the news, invest, and try to beat what the result would've been if you just held the stock instead\n")
    print("You will be playing from the perspective of an aging young adult who goes through his life.\n")

def apple_desc():
    print("\tApple, a tech company run by Steve Jobs, Steve Wozniak, and Ronald Wayne, has established itself as a key player in the PC market.")
    print("\tThey are well known for their innovative and user-friendly products, especially in their Macintosh line.")
    print("\tDespite seeing some ups and downs over the years, Apple is a recognizable brand in the industry.")

def intel_desc():
    print("\tIntel Corp, a tech hardware company with known for being the number one producer of semiconductor chips in the world")
    print("\tThey are well known for their x86 series which can be found in most computers.")
    print("\tThey have been seeing a dramatic rise in their stock price in recent years, cementing themselves as a very lucritive stock.")

def microsoft_desc():
    print("\tMicrosoft, A tech software company known for their windows operating system which has spread worldwide")
    print("\tThey have a strong presence in the market with a strong drive for innovation, setting standards for software nation-wide")

def end(bal, holding, temp_bal, temp_hold, price):
    print("you are now 41 years old and it is the year 2024.")
    print(f"As of now, you have an estimated networth of ${format (round(bal + (holding*price)), ',d')}")
    print("Even though Apple was an extremely successful company and is not a perfect example, lets see if you beat the game")
    print("Lets calculate what you could've had if you just bought and never sold")
    print(f"We can see that you could've had... ${format (round(temp_hold*price), ',d')} in just 23 years")
    if temp_hold*price > bal + (holding*price):
        print("\nYou can see that you did not beat the game...")
        print("There is a motto to always remember")
        print("\nTime in the market is always better than timing the market")
        print("\nI hope you always remember that")
        print("That you for playing my game, I hope you enjoyed :)")
    else:
        print("\nI am very impressed that you were able to beat the goal")
        print("It is very hard to beat just holding apple")
        print("very good job!")
        print("Even though you were able to win I would like to tell you a message")
        print("\nTime in the market is always better than timing the market")
        print("\nI hope you always remember that")
        print("That you for playing my game, I hope you enjoyed :)")