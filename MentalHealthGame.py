import sqlite3
import os
import random
database=sqlite3.connect("MentalHealthGame.db")
cursor=database.cursor()

class character:
    def __init__(self, id, name, difficulty, health, attack):
        self.id=id
        self.name=name
        self.difficulty=difficulty
        self.health=health
        self.attack=attack

def get_integer_input(min_input, max_input):
    user_input=-1
    while user_input<min_input or user_input>max_input:
        user_input=input(f"Please enter an integer between {min_input} and {max_input}: ")
        try:
            user_input=int(user_input)
        except:
            user_input=-1
    return user_input

os.system("cls")
print("Welcome to the Mental Health Sanctuary")
print("A game designed to help you learn all about mental illnesses")
print("What they are, how they present, and how to combat them all through a fantasy fighter game")
print("This game is not intended as diagnostic or health advice, it is for education only")
print("If you or someone you know is struggling, websites like the Mental Health Foundation will be more helpful")
input("If you are ready to learn, press enter ")

os.system("cls")
print("In this game you can pick to play through any of the following mental illnesses:")
cursor.execute("SELECT * FROM ILLNESS")
results=cursor.fetchall()
for mental_illness in results:
    print(f"{mental_illness[0]}. {mental_illness[1]}")
print("Please select an illness for this playthrough")
chosen_illness_id=get_integer_input(1,len(results))

os.system("cls")
chosen_illness_name=results[chosen_illness_id-1][1]
print(f"You chose {chosen_illness_name}")
cursor.execute(f"SELECT * FROM CHARACTER WHERE illness_id={chosen_illness_id}")
character_results=cursor.fetchall()
print("You can play through this illness with one of the following characters:")
for i in range(len(character_results)):
    print(f"{i+1}. {character_results[i][1]}")
    print(f"Difficulty level: {character_results[i][2]}")
    print(f"Health points: {character_results[i][3]}")
    print(f"Attack power: {character_results[i][4]}")
print("Please select a character")
character_reference_id=get_integer_input(1,len(character_results))
chosen_character=character(character_results[character_reference_id-1][0],character_results[character_reference_id-1][1],
                           character_results[character_reference_id-1][2],character_results[character_reference_id-1][3],
                           character_results[character_reference_id-1][4])

os.system("cls")
print(f"{chosen_character.name}, you wake in a healer's tent, your limbs feel heavy and your head is pounding")
print("You see your trainer looking down at you, concerned, and you ask them what happened")
print(f"They tell you that you were attack by a creature known as {chosen_illness_name}")
print("They say that you were lucky to make it out alive, but it won't stop coming for you")
print("You need to defeat it, and you can if you break it up into smaller fights, but first you need to rest")
print("We'll tackle this when you're feeling better")
input("Press enter to continue ")