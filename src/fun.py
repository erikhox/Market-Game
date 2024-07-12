import os

#All these little functions are just events that happen during the players life
def new_grad_job(cash):
    cash += 56000
    print("-"*50)
    print(f"Event: ")
    print("\nYou got your first job, your salary is starting at $56,000")
    print("-"*50) 
    return cash
    
def promotion(cash):
    cash *= 1.15
    print("-"*50)
    print(f"Event: ")
    print("\nYou got a promotion, your salary goes up 15 percent")
    print("-"*50) 
    return cash

def sal_raise(cash):
    cash *= 1.03
    print("-"*50)
    print(f"Event: ")
    print("\nYou got a raise, your salary goes up 3 percent")
    print("-"*50) 
    return cash

def child(cash):
    cash -= 12000
    print("-"*50)
    print(f"Event: ")
    print("\nYou had a kid, you need to pay $12,000 a year")
    print("-"*50) 
    return cash

def living(cash):
    cash -= 22800
    print("-"*50)
    print(f"Event: ")
    print("\nYou need to pay for basic living expenses, you pay $22,800 a year")
    print("-"*50) 
    return cash

def house(cash):
    cash -= 6000
    print("-"*50)
    print(f"Event: ")
    print("\nYou have bought a house, your income goes down $6000")
    print("-"*50)   
    return cash

#This function is for when the player chooses a stock, it ends up always being apple at the end
def choose(choice, intel, microsoft):
    while True:
        if choice == "INTC" and intel == False:
            intel = True
            if microsoft == True and intel == True:
                print("\tYou were too scared to invest as you didn't understand what microprocessors even were...")
                print("\tYou looked at your desk and you see you are using a macintosh, you decide to invest in Apple Computer Inc...")
                break 
            print("\tYou were too scared to invest as you didn't understand what microprocessors even were...")
            choice = input("Please enter one of the stocks to start (AAPL, MSFT): ")

        elif choice == "MSFT" and microsoft == False:
            microsoft = True
            if microsoft == True and intel == True:
                print("\tYour parents complained about you investing in Microsoft, they made you do soemthing else...")
                print("\tYou looked at your desk and you see you are using a macintosh, you decide to invest in Apple Computer Inc...")
                break 
            print("\tYour parents complained about you investing in Microsoft, they made you do soemthing else...")
            choice = input("Please enter one of the stocks to start (AAPL, INTC): ")

        elif choice == "AAPL":
            print("\tYou looked at your desk and you see you are using a macintosh, you decide to invest in Apple Computer Inc...")
            break

        elif intel == True:
            print("\tI dont seem to quite understand...")
            choice = input("Please enter one of the stocks to start (AAPL, MSFT): ")

        elif microsoft == True:
            print("\tI dont seem to quite understand...")
            choice = input("Please enter one of the stocks to start (AAPL, INTC): ")

        else:
            print("\tI dont seem to quite understand...")
            choice = input("Please enter one of the stocks to start (AAPL, INTC, MSFT): ")

#this prints information
def screen(date, age, bal, num_stock, income, current_price, news, temp):
    print(f"The date is currently {date}")
    print(f"You are {age} years old")
    print(f"your current balance is ${bal}")
    print(f"you currently hold {num_stock} AAPL shares worth ${num_stock*current_price}")
    print(f"you currently put away ${round(income/10)} every year to spend on stocks")
    print(f"AAPL stock is currently priced at {current_price}")
    if date == "10/1/2023":
        print("-"*50)
        print(f"current news: ")
        print(f"\t{news.iloc[temp,1]}")
        print("-"*50)
    elif date == news.iloc[temp,0]:
        print("-"*50)
        print(f"current news: ")
        print(f"\t{news.iloc[temp,1]}")
        print("-"*50)        
        temp += 1
    return temp

#this function is where the logic behind buying, selling, and holdings stocks happen
def action(price_of_stock, current_balance, current_holdings):

    choice = input("\nWhat would you like to do (buy, sell, hold (press enter to auto-hold)): ")

    while True:
        if choice == "buy":
            print("\nYou have decided to buy some AAPL shares...")
            amount = int(input("How much shares would you like to purchase: "))
            if amount * price_of_stock <= current_balance:
                current_holdings += amount
                print(f"you have purchases {current_holdings} shares of AAPL")
                current_balance -= current_holdings * price_of_stock
                break
            elif amount * price_of_stock > current_balance:
                print("You can not purchase that many shares...")
                choice = input("What would you like to do (buy, sell, hold): ")
                continue

        elif choice == "sell":
            print("\nYou have decided to sell some AAPL shares...")
            amount = int(input("How much shares would you like to sell: "))
            if amount < current_holdings:
                current_holdings -= amount
                print(f"you have sold {current_holdings} shares of AAPL")
                current_balance += amount * price_of_stock
                break
            elif amount > current_holdings:
                print("You can not sell that many shares...")
                choice = input("What would you like to do (buy, sell, hold): ")
                continue
        elif choice == "hold" or choice == "":
            print("\nyou have decided to hold off on purchasing or selling any stocks...")
            break
        else:
            print("\nI dont seem to understand")
            choice = input("What would you like to do (buy, sell, hold): ")
    input("\nPlease press enter to proceed to the next month (press enter): ")
    os.system('cls')
    return current_balance, current_holdings 