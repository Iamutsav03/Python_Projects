import random

print("Are you ready to paly")
Range = input("Select The Range ")

if(Range.isdigit()):
    Range = int(Range)
    if(Range <= 0):
        print("Please write a number greater then 0")
else:
    print("Please write a number") 

print("Now Start guessing your Number")
turn = 0
number = random.randint(1 , Range)
while(True):
    turn += 1
    guess = input("Your Guess --> ")
    if(guess.isdigit()):
        guess = int(guess)
    else:
        print("Please write a number")
        
    if(guess <= 0 or guess > Range):
        print("Please write a number that is in range (<= 1 and >=" + str(Range) + ')')
    elif(guess == number):
        print("Congrats! you guessed it right ")
        print("You Took " + str(turn) + " Turns")
        break
    elif(guess > number):
        print ("your guess was greater then number, you have took "+ str(turn) +" turn till now")
    elif(guess < number):
        print ("your guess was smaller then number, you have took "+ str(turn) +" turn till now")