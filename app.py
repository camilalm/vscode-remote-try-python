#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

print("Welcome to Minigame!")

continue_game = True
player_scoreboard = { "wins": 0, "losses": 0, "ties": 0 }
while continue_game:
    option = input("Enter an option to play (R) rock (P) paper or (S) scissors: ")
    option = option.upper()
    if option not in ["R", "P", "S"]:
        print("Invalid option!")
    else:
        computer_option = random.choice(["R", "P", "S"])
        print("Computer option: ", computer_option)
        if option == computer_option:
            print("Tie!")
            player_scoreboard["ties"] = player_scoreboard["ties"] + 1
        elif option == "R" and computer_option == "S":
            print("You win!")
            player_scoreboard["wins"] = player_scoreboard["wins"] + 1
        elif option == "P" and computer_option == "R":
            print("You win!")
            player_scoreboard["wins"] = player_scoreboard["wins"] + 1
        elif option == "S" and computer_option == "P":
            print("You win!")
            player_scoreboard["wins"] = player_scoreboard["wins"] + 1
        else:
            print("You lose!")
            player_scoreboard["losses"] = player_scoreboard["losses"] + 1
    print("Player Scoreboard: ", player_scoreboard)
    # verify continue_game is either Y or N
    while continue_game not in ["Y", "N"]:
        continue_game = input("Do you want to continue? (Y) yes or (N) no: ").upper()
        if continue_game not in ["Y", "N"]:
            print("Invalid option!")
    continue_game = continue_game == "Y"    
print("Thanks for playing!")
exit()