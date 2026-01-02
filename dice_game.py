import random

users = []
num_of_users = int(input("Number of players want to play this game? "))

for i in range(num_of_users):            
    users.append(f"user{i}")                          

max_score = 0
scores = [0] * num_of_users               

while max_score < 50:

    for user in range(num_of_users):

        user_score = scores[user]

        while True:
            ask_turn = input(f"Hey {users[user]}, do you want to roll or pass (y/n)? ")

            if ask_turn.lower() == 'y':
                cur_num = random.randint(1, 6)
                print(f"You rolled: {cur_num}")

                if cur_num == 1:
                    user_score = 0
                    scores[user] = user_score
                    print("Oops! You rolled a 1. Your turn ends.")
                    break  

                else:
                    user_score += cur_num
                    scores[user] = user_score
                    print(f"Your score is now {user_score}")

                

            elif ask_turn.lower() == 'n':
                print("You passed your turn.")
                break  

            else:
                print("Please only answer y or n")

    max_score = max(max_score, user_score)
    if max_score >= 50:
        break

 