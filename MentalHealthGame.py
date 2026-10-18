import sqlite3
import os
import random
database=sqlite3.connect("MentalHealthGame.db")
cursor=database.cursor()

print("Welcome to the Mental Health Sanctuary")
print("A game designed to help you learn all about mental illnesses")
print("What they are, how they present, and how to combat them all through a fantasy fighter game")
print("This game is not intended as diagnostic or health advice, it is for education only")
print("If you or someone you know is struggling, websites like the Mental Health Foundation will be more helpful")
input("If you are ready to learn, press enter")
os.system("cls")
print("In this game you can pick to play through any of the following mental illnesses:")
cursor.execute("SELECT * FROM ILLNESS")
results=cursor.fetchall()
for i in results:
    print(str(i[0])+'.', i[1])
chosen_illness_id=input(f"Select an illness to play through by typing a number 1 through {len(results)}: ")