# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:55:11 2019

@author: Admin
"""
from time import sleep
from random import randint

responses = ["It is certain.",
"It is decidedly so."
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]

def game():
    input("Enter your question: ")
    print("\nThinking...\n")
    sleep(5)
    a = randint(0, 20)
    print(responses[a])
    response = input("\nDo you want to play again? Enter Y/N\n")
    if(response.upper() == 'Y'):
        game()
    elif(response.upper() == 'N'):
        print("Thanks for playing!")
    else:
        print("You have entered the wrong choice. Thanks for playing")
game()

    


