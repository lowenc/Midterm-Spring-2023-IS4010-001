# Name: Nathan Lowe
# Email: lowenc@mail.uc.edu
# Assignment Title: Midterm
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This project required modifying code to add error handling
# Citations:    https://www.w3schools.com/python/gloss_python_error_handling.asp
# Anything else that's relevant:

# main.py

from videoGamePackage.videoGame import *

totalPlays = 1000
won = 0
lost = 0
for i in range(0, totalPlays):

    try:
        if play():
            won = won + 1
        else:
            lost = lost + 1
    except:
        pass
percentageWon = won / totalPlays
print(f"Total Plays: {totalPlays} , Won = {won} , Lost = {lost} Percentage Won = {percentageWon}")