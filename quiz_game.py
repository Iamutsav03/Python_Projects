print("Hello , Welcome to the quiz game")
start = input("Are you ready to play? ")
if(start.lower() != 'yes'):
    quit()
else:
    print("ok Lets play")

score = 0
answer = input("What CPU stands for? ")
if(answer.lower() == 'central processing unit'):
    print("its correct!!")
    score += 3
else:
    print("its wrong")
    score -= 1
answer = input("What GPU stands for? ")
if(answer.lower() == 'graphics processing unit'):
    print("its correct!!")
    score += 3
else:
    print("its wrong")
    score -= 1
    
print("your score is" + str(score) + " , Thanks for playing")