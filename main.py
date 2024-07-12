from src.Text import *
from src.fun import *
import os
import pandas as pd
import random

aapl_data = pd.read_csv('data/AAPL.csv')
aapl_news = pd.read_csv('data/AAPL_NEWS.csv')

#This is the first screen to show users and to describe the premise of the game
title()
welcome()
ans = input("Are you ready to begin (y/n):")
ready = False

while ready == False:
    if ans == "y":
        ready = True
        os.system('cls')
    elif ans == "n":
        print("Try again")
        ans = input("(y/n): ")
    else:
        print("I don't seem to understand.")
        ans = input("(y/n): ")

#this section is to tell the user about the different stocks to trade in and for the user to choose a stock
print("Here are your options for what stocks to invest in.")
print("-"*150)
print("Apple - AAPL")
apple_desc()
print("\nIntel - INTC")
intel_desc()
print("\nMicrosoft - MSFT")
microsoft_desc()
print("-"*150)
print()
choice = input("Please enter one of the stocks to start (AAPL, INTC, MSFT): ")

#variables just to use quickly for stock selection
int = False
ms = False

#called the function to choose the stock
choose(choice, int, ms)

print("\tGood choice...")
input("\nPress enter to continue")
os.system('cls')

#initlizing beginning variables
age = 18
balance = 3000
holdings = 0
income = 0
invest_cash = (1/120)
date = aapl_data.iloc[0,0]
price = float(aapl_data.iloc[0,1])
temp = 0
home = False
graduated = False
children = 0

#these variables are used to find the goal
goal = 0
temp_bal = 3000

#this is the loop for trading stocks, it keeps going from 1/1/2000 to 12/1/2023
for i in range(1,24*12):
    chance = random.random()
    temp = screen(date, age, balance, holdings, income, price, aapl_news, temp)
    if (i) % 12 == 0:
        age += 1
    date = aapl_data.iloc[i,0]
    price = float(aapl_data.iloc[i,1])
    if graduated == False and age >= 23 and chance >= 0.9:
        income = new_grad_job(income)
        income = living(income)
        round(income)
        graduated = True
    if home == False and age >= 30 and chance > 0.5:
        income = house(income)
        round(income)
        home = True
    if age >= 28 and chance <= chance-children:
        if children == 0:
            children += 0.1
            income = child(income)
            round(income)
        else:
            children *= 0.5
            income = child(income)
            round(income)
    if graduated == True:
        if chance >= .98:
            income = promotion(income)
            round(income)
        elif chance >= .95:
            income = sal_raise(income)
            round(income)
    balance += invest_cash * income
    temp_bal += invest_cash * income
    balance, holdings = action(price, balance, holdings)

    while True:
        if temp_bal - price > 0:
            temp_bal -= price
            goal += 1
        else:
            break

#outputs ending message
end(balance, holdings, temp_bal, goal, price)
input("\npress enter to quit")