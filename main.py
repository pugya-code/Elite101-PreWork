import random

print("Welcome to this chatbox user!! tell us about yourself. :)")
user_input = input("type in 'yes'to keep the program going or 'q' to stop\n")

##def quit_method ():
## quit_chara = 'q'

if user_input != 'q' :
    name = (str(input('What is your name?\n')))
    while name.isnumeric():
        print("Your name is a number? is that even legal?!?! Try again!!")
        name = input('What is your name?\n')

    print("wow " + name + " you have a wonderful name!!")
    print("Anyway, how is your day? good, bad, other?")
    feelings = input("tell me all about it :)")
    print(
        "woahhh, thats pretty interesting!! I have to ask, do you have any pets?"
    )
    pets = input("if not, type no!!")

    if pets == "no":
        print("aww man, we can always talk about something else!!")

    else: 
        print("WOAH! they sound awesome")
    
      