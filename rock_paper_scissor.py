import random 

options = ['r' , 'p' , 's']
user_score = 0
comp_score = 0
rounds = int(input("Lets Start the Game! Are you ready? Select number of rounds "))
total_rounds = rounds
while rounds:
    num = random.randint(0 , 2)
    comp = options[num]
    
    user = input("what you choose?type...R(rock) or P(paper) or S(scissor) ")
    if(user not in options.lower()):
        print("please choose only between (R , P , S)...")
    else:
        if((user == 'r' and comp == "s" )or (user == 'p' and comp == "r") or (user == 's' and comp == "p")):
            user_score += 1
        elif(user == comp):
            print("this round tied")
        else:
            comp_score += 1
    xyz = total_rounds - rounds +1
    print("BY ROUND "+ str(xyz) +" SCORE IS ")
    print("User ---> "+ str(user_score))
    print("Computer ---> "+ str(comp_score))
    rounds -= 1
