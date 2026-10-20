import sqlite3
import os
import random
database=sqlite3.connect("MentalHealthGame.db")
cursor=database.cursor()

def get_integer_input(min_input, max_input):
    user_input=-1
    while user_input<min_input or user_input>max_input:
        user_input=input(f"Please enter an integer between {min_input} and {max_input}: ")
        try:
            user_input=int(user_input)
        except:
            user_input=-1
    return user_input

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
print("Please select an illness for this playthrough")
chosen_illness_id=get_integer_input(1,len(results))