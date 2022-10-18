import random

while True:
    try:
        rounds = int(input("How many rounds do you want to play? \n"))

        i = 1
        player_count = 0
        bot_count = 0

        while i <= rounds:
            rps = (input("Choose! Rock, Paper, Scissors: \n"))
            bot = int(random.randint(1, 3))

            r_psi = 0

            if rps == "Rock":
                r_psi = 1
            elif rps == "Paper":
                r_psi = 2
            elif rps == "Scissors":
                r_psi = 3

            bot_out = ""

            if bot == 1:
                bot_out = "Rock"
            elif bot == 2:
                bot_out = "Paper"
            elif bot == 3:
                bot_out = "Scissors"

            print(f"Round {i}: {rps} vs {bot_out}")

            # print(rps)
            # print(bot)

            if r_psi == 1 and bot == 1 or r_psi == 2 and bot == 2 or r_psi == 3 and bot == 3:
                print("Its a tie!")
                print(f"Player: {player_count} vs Bot: {bot_count} \n")
            elif r_psi == 1 and bot == 2 or r_psi == 2 and bot == 3 or r_psi == 3 and bot == 1:
                print("The bot wins!")
                bot_count += 1
                print(f"Player: {player_count} vs Bot: {bot_count} \n")
            elif r_psi == 1 and bot == 3 or r_psi == 2 and bot == 1 or r_psi == 3 and bot == 2:
                print("The player wins!")
                player_count += 1
                print(f"Player: {player_count} vs Bot: {bot_count} \n")

            i += 1

    except ValueError:
        print("Wrong Input, try again")

    exit()
