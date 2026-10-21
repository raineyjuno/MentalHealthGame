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

class management:
    def __init__(self, name, effectivity, boost, value):
        self.name=name
        self.effectivity=effectivity
        self.boost=boost
        self.value=value

class symptom:
    def __init__(self, name, difficulty, health, attack):
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

os.system("cls")
print(f"{chosen_character.name}, it's time to start fighting")
print("Everyday you will fight the most manageable part of this creature that you haven't yet defeated")
print("Before each fight I will offer you a management tool that you can choose to use for a mystery boost")
print("If you lose the fight you will restart the day and lose your boost, but if you win you learn to manage the symptom and gain a boost")
print("There are 5 levels, and once you overcome all of them you win the game")
input("Press enter to continue ")

defeated_symptoms=0
cursor.execute(f"""SELECT MANAGEMENT.name, ILLNESS_MANAGEMENT.* 
                    FROM MANAGEMENT, ILLNESS_MANAGEMENT 
                    WHERE ILLNESS_MANAGEMENT.illness_id={chosen_illness_id}  
                    AND MANAGEMENT.id=ILLNESS_MANAGEMENT.management_id
                    ORDER BY ILLNESS_MANAGEMENT.effectivity_ranking""")
all_managements=cursor.fetchall()
first_management=management(all_managements[0][0],1,all_managements[0][4],all_managements[0][5])
# individual variables for next 4
while defeated_symptoms<5:
    os.system("cls")
    print(f"Day {defeated_symptoms+1}")
    print(f"Your starting stats are {chosen_character.health} health points and {chosen_character.attack} attack power")
    cursor.execute(f"""SELECT MANAGEMENT.name, ILLNESS_MANAGEMENT.* 
                    FROM MANAGEMENT, ILLNESS_MANAGEMENT 
                    WHERE ILLNESS_MANAGEMENT.illness_id={chosen_illness_id} 
                    AND ILLNESS_MANAGEMENT.effectivity_ranking={defeated_symptoms+1} 
                    AND MANAGEMENT.id=ILLNESS_MANAGEMENT.management_id""")
    management_info=cursor.fetchall()
    current_management=management(management_info[0][0],defeated_symptoms+1,management_info[0][4],management_info[0][5])
    print(f"Hello {chosen_character.name}, today I offer you {current_management.name.lower()}")
    print("Would you like to try it?")
    management_choice=""
    while management_choice.lower()!="y" and management_choice.lower()!="n":
        management_choice=input("Please enter y for yes or n for no: ")
    health_boost=0
    attack_boost=0
    if management_choice.lower()=="y":
        if current_management.boost.lower()=="health":
            health_boost=current_management.value
            print(f"You have received a boost of {current_management.value} to your health")
        elif current_management.boost.lower()=="attack":
            attack_boost=current_management.value
            print(f"You have received a boost of {current_management.value} to your attack")
        else:
            health_boost=current_management.value
            attack_boost=current_management.value
            print(f"You have received a boost of {current_management.value} to your health and your attack")
    input("Press input to enter the fight ")

    os.system("cls")
    cursor.execute(f"""SELECT SYMPTOM.name, ILLNESS_SYMPTOM.*
                    FROM SYMPTOM, ILLNESS_SYMPTOM
                    WHERE ILLNESS_SYMPTOM.illness_id={chosen_illness_id}
                    AND ILLNESS_SYMPTOM.difficulty_ranking={defeated_symptoms+1}
                    AND SYMPTOM.id=ILLNESS_SYMPTOM.symptom_id""")
    symptom_info=cursor.fetchall()
    current_symptom=symptom(symptom_info[0][0],defeated_symptoms+1,symptom_info[0][4],symptom_info[0][5])
    print(f"You are now going to fight {current_symptom.name}")
    print(f"It has {current_symptom.health} health points and {current_symptom.attack} attack power")
    damage_done=0
    damage_taken=0
    while damage_taken<chosen_character.health+health_boost:
        print(f"You have {chosen_character.health+health_boost-damage_taken} health points remaining")
        input(f"Press enter to hit for {chosen_character.attack+attack_boost} points")
        damage_done+=chosen_character.attack+attack_boost
        if damage_done>=current_symptom.health:
            break
        print(f"You dealt {chosen_character.attack+attack_boost} damage and it now has {current_symptom.health-damage_done} health")
        damage_taken+=current_symptom.attack
        print(f"It hits back for {current_symptom.attack} points")
    if damage_taken>=chosen_character.health+health_boost:
        print("")
        print("Unforunately you have been bested")
        print("Your boosts will be removed and you will restart this day in order to try again")
        input("Press enter to try again ")
    else:
        print("")
        print(f"Congratulations, you have learnt to manage {current_symptom.name}")
        print(f"You can choose to take a boost of {current_symptom.health//2} to your health or {current_symptom.attack//2} to your attack")
        boost_choice=""
        while boost_choice.lower()!="h" and boost_choice.lower()!="a":
            boost_choice=input("Please enter h for health or a for attack: ")
        if boost_choice.lower()=="h":
            chosen_character.health+=current_symptom.health//2
        else:
            chosen_character.attack+=current_symptom.attack//2
        chosen_character.health+=health_boost
        chosen_character.attack+=attack_boost
        defeated_symptoms+=1
        print("Your boosts have been added to your character stats")
        input("Press enter to begin the next day ")

os.system("cls")
print("You wake and your head feels clearer than it has in a long time")
print("You look to your trainer, ready to be offered a management tool, but they shake their head")
print("You ask if you're done, if it's finally gone, and they shake their head again")
print("Not gone, they tell you, you just know how to live with it now")
input("Press enter to finish the game ")
os.system("cls")
print(f"Congratulations! You have learnt some strategies to deal with {chosen_illness_name}")
print("You now get to immortalise your initials in the scoreboard!")
users_initials=""
while len(users_initials)!=2:
    users_initials=input("Please enter 2 characters to represent you on the scoreboard: ")
cursor.execute(f"INSERT INTO SCOREBOARD (name_of_player, illness_id, character_id) VALUES ('{users_initials}',{chosen_illness_id},{chosen_character.id})")
database.commit()
cursor.execute(f"""SELECT SCOREBOARD.name_of_player, ILLNESS.name, CHARACTER.name
                FROM SCOREBOARD, ILLNESS, CHARACTER
                WHERE ILLNESS.id=SCOREBOARD.illness_id
                AND CHARACTER.id=SCOREBOARD.character_id""")
scoreboard=cursor.fetchall()
os.system("cls")
for entry in scoreboard:
    print(f"{entry[0]} successfully played through {entry[1]} with {entry[2]}")