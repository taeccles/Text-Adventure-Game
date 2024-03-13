from colorama import Fore, Style
import time
import os

# ***Charcter Visit Global Tracker***
doc_visit = False
gen_visit = False
prof_visit = False

def show_credits():
    typewriter_effect("")
    typewriter_effect("Game Credits:")
    typewriter_effect("🅜🅐🅝🅨")
    typewriter_effect("🅟🅔🅓🅡🅞")
    typewriter_effect("🅣🅗🅞🅜🅐🅢")
    typewriter_effect("🅚🅐🅨🅣🅛🅘🅝")
    typewriter_effect("🅑🅘🅝🅘🅐🅜")
    typewriter_effect("🅤🅜🅔")
    typewriter_effect("🅜🅞🅗🅐🅜🅔🅓")
    


# Function to simulate typewriter effect - Manny's Work
def typewriter_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.0)  # Adjust the sleep time for desired speed
    print()


# --Ready to accuse or continue interrogating
def accuse_or_continue():
    typewriter_effect("")
    typewriter_effect("Would you like to accuse someone or continue interrogating remaining suspects?")
    choice = input(Fore.YELLOW + "type 'accuse' or 'continue': " + Style.RESET_ALL).lower()
    if choice == 'accuse':
        guess_suspect()
    elif choice == 'continue':
        return
    else:
        typewriter_effect("")
        typewriter_effect("Invalid choice! Please type 'accuse' or 'continue'.")
        accuse_or_continue()


#--Refresh all suspect visit globals--
def refresh_visits():
    global doc_visit, gen_visit, prof_visit
    doc_visit = False
    gen_visit = False
    prof_visit = False


#--Game restart--
def game_restart():

    typewriter_effect(Fore.RED + "Game Over!! 💀" + Style.RESET_ALL)
    exit_game = False

    while not exit_game:
        typewriter_effect("")
        user_restart = input(Fore.BLUE + "Would you like to restart? Type 'yes' or 'no': " + Style.RESET_ALL).lower()

        if user_restart == "yes":
            intro()
        elif user_restart == "no":
            typewriter_effect("")
            typewriter_effect(Fore.YELLOW + "Goodbye, thanks for playing :)" + Style.RESET_ALL)
            show_credits()
            quit()
        else:
            typewriter_effect("")
            typewriter_effect("Invalid input! Please type 'yes' or 'no'.")


#--Game Win Restart--
def game_win_restart():
    exit_game = False
    while not exit_game:
        user_restart = input(Fore.GREEN + "Would you like to restart? Type 'yes' or 'no': " + Style.RESET_ALL).lower()

        if user_restart == "yes":
            intro()
        elif user_restart == "no":
            typewriter_effect("")
            typewriter_effect("Goodbye, thanks for playing :)")
            quit()
        else:
            typewriter_effect("")
            typewriter_effect("Invalid input! Please type 'yes' or 'no'.")


#--Introduction
def intro():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    refresh_visits()
    typewriter_effect("As Dr. John Watson, Sherlock Holmes's faithful partner, ")
    typewriter_effect("you woke up to the chilling news of Sherlock's untimely demise.") 
    typewriter_effect("The world feels darker without his keen intellect and sharp wit.")
    typewriter_effect("")
    typewriter_effect("Summoned to London to investigate the mysterious circumstances surrounding Sherlock's death, ")
    typewriter_effect("you find yourself at 221B Baker Street, where your dear friend once resided.")
    typewriter_effect("The air is heavy with the weight of unanswered questions and looming danger.") 
    typewriter_effect("")
    typewriter_effect("What secrets lie within these walls? It's up to you to uncover the truth and ")
    typewriter_effect("bring justice to Sherlock's memory.")
    typewriter_effect("What would you like to do?")
    
    while True:
        typewriter_effect("")
        typewriter_effect("Search Sherlock's body? or Flee the scene?")
        choice = input(Fore.YELLOW + "type 'search 🔍' or 'flee 🏃': " + Style.RESET_ALL).lower()

        if choice == "search":
            typewriter_effect("")
            typewriter_effect("You have found a revolver and a diary with the list of people Sherlock has seen yesterday")
            typewriter_effect("After going through the diary you have found 3 names: ")
            suspects_main()
            break
        elif choice == "flee":
            typewriter_effect("")
            typewriter_effect("You have fled the scene raising suspicion and becoming the prime suspect yourself! ")
            typewriter_effect("...Probably not the best idea Watson")
            typewriter_effect("You are a bad detective.. ")
            game_restart()
            break
        else:
            typewriter_effect("Invalid choice! Please enter 'search' or 'flee'.")


#--Interrogating the 3 Suspects
def suspects_main():
    global doc_visit, gen_visit, prof_visit

    typewriter_effect("")
    typewriter_effect(Fore.BLUE + "Suspects: ")
    typewriter_effect("- Doctor Johnathan Wiles 👨‍⚕️ ")
    typewriter_effect("- Professor Abigail Thorne 👩‍🏫 ")
    typewriter_effect("- General Blackwood 👨‍⚖️ " + Style.RESET_ALL)

    while not all([doc_visit, prof_visit, gen_visit]):
        typewriter_effect("")
        typewriter_effect("Who would you like to interrogate?")
        suspect_visit = input(Fore.YELLOW +"Type 'Doctor' or 'Professor' or 'General': " + Style.RESET_ALL).lower()

        if suspect_visit == "doctor" and not doc_visit:
            doctor()
            accuse_or_continue()
            doc_visit = True

        elif suspect_visit == "professor" and not prof_visit:
            professor()
            accuse_or_continue()
            prof_visit = True

        elif suspect_visit == "general" and not gen_visit:
            general()
            accuse_or_continue()
            gen_visit = True

        else:
            typewriter_effect("Invalid input! Please enter the name of one of the remaining suspects.")

    # If all suspects have been visited, prompt for accusing
    guess_suspect()


#--Doctor Character
def doctor():
    typewriter_effect("")
    typewriter_effect("You have arrived at the Hospital, walking past the busy corridors you spot a nurse who gladly directs you to Doctor.. ")
    typewriter_effect("...(because you are 10/10 charming )")
    typewriter_effect("")
    typewriter_effect("Doctor Wiles is now standing in front of you: Can I help you?")
    typewriter_effect("")
    typewriter_effect("What is your response? Will you show him the diary and ask more questions? ")
    typewriter_effect("Or will you show him the gun and see what he knows?")

    while True:
        choice = input(Fore.YELLOW + "type 'gun 🔫' or 'diary 📓': " + Style.RESET_ALL).lower()

        if choice == "diary":
            typewriter_effect("")
            typewriter_effect("I know nothing of these people.. why are you asking me this?! ")
            typewriter_effect("I'm busy now leave me alone..")
            break
        
        elif choice == "gun":
            typewriter_effect("")
            typewriter_effect("Are you crazy??! this is a hospital!! GET OUT!")
            break
    
        else:
            typewriter_effect("")
            typewriter_effect("Invalid input! Please enter 'gun' or 'diary'.")


#--Professor Character
def professor():
    typewriter_effect("")
    typewriter_effect("You have arrived at the University, ")
    typewriter_effect("walking past the classrooms you spot a professor who notices you snooping and she seems distressed.")
    typewriter_effect("")
    typewriter_effect("Professor Abigail Thorne is now standing in front of you: ")
    typewriter_effect("What are you doing here?! Who gave you access to this area?")
    typewriter_effect("")
    typewriter_effect("The Professor starts playing with her hair nervously and looking around for help.")
    typewriter_effect("You must act quickly, Watson, before she causes a scene.") 
    typewriter_effect("Will you show her the diary? Or will you show her the gun and see what she knows? ")
    
    while True:
        choice = input(Fore.YELLOW + "type 'gun 🔫' or 'diary 📓': " + Style.RESET_ALL).lower()

        if choice == "diary":
            typewriter_effect("")
            typewriter_effect("I'm not familiar with this diary, but I know the General. ") 
            typewriter_effect("He was supposed to speak at the university campus last night.. ")
            typewriter_effect("but he never showed up...")
            break
        
        elif choice == "gun":
            typewriter_effect("")
            typewriter_effect("* Are you crazy??! Why do you have a gun!? ")
            typewriter_effect("The Professor becomes extremely scared and begins to have a heart attack")
            typewriter_effect("You try your best to perform CPR on her but you cannot do enough to save her.")
            game_restart()
            break
        
        else:
            typewriter_effect("")
            typewriter_effect("Invalid input! Please enter 'gun' or 'diary'.")


#--General Character
def general():
    typewriter_effect("")
    typewriter_effect("You head to the General's Office. He does not look happy...") 
    typewriter_effect("General: YOU BETTER BE QUICK!!!!")
    typewriter_effect("Would you like to 'show gun' or 'show 'diary?")
    
    while True:
        choice = input(Fore.YELLOW + "Type 'gun 🔫' or 'diary 📓': " + Style.RESET_ALL).lower()

        if choice == "gun":
            typewriter_effect("")
            typewriter_effect("You reach into your pocket for the revolver.")
            typewriter_effect("The General is quick to react and SHOOTS YOU!")
            game_restart()
            break
            
        elif choice == "diary":
            typewriter_effect("")
            typewriter_effect("You show the General the List...")
            typewriter_effect("He suspiciously glances and looks back at you.")
            typewriter_effect("I was a guest speaker at the university last night.")
            typewriter_effect("He pushes you out. I DON'T HAVE TIME FOR THIS!!")
            break
            
        else:
            typewriter_effect("Invalid input! Please enter 'gun' or 'diary'.")


#--Ready to guess?          
def guess_suspect():
    typewriter_effect("")
    typewriter_effect("You have now visited all the suspects... ")
    typewriter_effect("All your work has been leading to this point... ")
    typewriter_effect("Are you ready to choose..? ")

    while True:
        choice = input (Fore.YELLOW + "type 'yes' or 'no': " + Style.RESET_ALL).lower()

        if choice == "no":
            typewriter_effect("")
            typewriter_effect("You are a bad detective..")
            game_restart()
            break
        elif choice == "yes":
            final_suspect()
            break
        else:
            typewriter_effect("Invalid input! Please enter 'yes' or 'no'.")


#--Finale:  Choose a Suspect!
def final_suspect():

    typewriter_effect("")
    typewriter_effect("Who would you like to choose?? ")
    typewriter_effect(Fore.BLUE + "Doctor Johnathan 👨‍⚕️  ")
    typewriter_effect("Professor Abigail 👩‍🏫  ")
    typewriter_effect("General W.B 👨‍⚖️ ")
    typewriter_effect("Jenny the tutor 👩‍🎓 " + Style.RESET_ALL)
    
    while True:
        typewriter_effect("")
        suspect_choice = input(Fore.YELLOW + "Type doctor, general, professor or jenny: " + Style.RESET_ALL).lower()

        if suspect_choice == "jenny": 
            typewriter_effect("")
            typewriter_effect("How dare you! She wasn't even born yet...")
            game_restart()
            break
       
        elif suspect_choice == "general":
            typewriter_effect("")
            typewriter_effect("You found the murderer!!! General William Blackwood")
            typewriter_effect("Sherlock was investigating a case involving corruption within the country's military defense matters, ")
            typewriter_effect("and the General was behind it all!!!")
            typewriter_effect("By eliminating Sherlock, the General hoped to bury the truth and protect his own interests.")
            #Game Win text
            typewriter_effect("")
            typewriter_effect(Fore.GREEN + "Congratulations, Detective! ")
            typewriter_effect("Your keen instincts and perseverance have uncovered the darkest of secrets.")
            typewriter_effect("Wooooooooo hoooooooooo")
            typewriter_effect("You win!🏆" + Style.RESET_ALL)
            show_credits()
            game_win_restart()
        
        elif(suspect_choice == "professor"):
            typewriter_effect("")
            typewriter_effect("Unfortunately, you accused the wrong suspect.")
            typewriter_effect("Poor Professor Thorne! ")
            typewriter_effect("She had no motive for this crime.")
            game_restart()  
        
        elif(suspect_choice == "doctor"):
            typewriter_effect("")
            typewriter_effect("Unfortunately, you accused the wrong suspect. Poor Doctor Wiles! ") 
            typewriter_effect("He had no motive for this crime, ")
            typewriter_effect("Who will look after his children now that he is in jail")
            game_restart()
        else:
            typewriter_effect("Invalid choice. Please enter the name of one of the four choices.")
        

           

# Initializes the Game
def main():
    intro()

main()