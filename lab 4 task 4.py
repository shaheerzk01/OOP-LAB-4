# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:25:53 2021

@author: 21A-003-SE
"""
import random
user_won=0
bot_won=0
while True:
    bot = random.randint(1,3)
    if bot == 1:
        bot = "rock"
    elif bot == 2:
        bot = "paper"
    elif bot == 3:
        bot = "scissors"
        
    user=input("Enter rock paper or scissors: ")
    print("Bot Chose:",bot)
    if user == bot:
        result = "tie"
    else:
        if user == "rock" and bot == "scissors":
            result = "User won , Bot lose"
            user_won += 1
        elif user == "paper" and bot == "rock":
            result = "User won, Bot lose"
            user_won += 1
        elif user == "scissors" and bot == "paper":
            result = "User won, Bot lose"
            user_won += 1
        elif bot == "rock" and user == "scissors":
            result = "Bot won , User lose"
            bot_won += 1
        elif bot == "paper" and user == "rock":
            result = "Bot won, User lose"
            bot_won += 1
        elif bot == "scissors" and user == "paper":
            result = "Bot won, User lose"
            bot_won += 1
    print(result)
    print("User Won:",user_won)
    print("Bot Won:",bot_won)
    if user_won > 2:
        print("!!!USER WON!!!")
        break
    elif bot_won > 2:
        print("!!!BOT WON!!!")
        break