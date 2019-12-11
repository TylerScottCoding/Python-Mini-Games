import random, string

print("Welcome to Rock Paper Scissor in Python!")
name = input("Please enter your name: ")
print(f"Hello {name}, to play simply enter 'r' for rock, 's' for scissors, or 'p' for paper when prompted.")
playing = True
while playing == True:
    play = input("Enter your play now: ")
    if play == 'p' or play == 's' or play == 'r':
        def randomrps():
            letters = ['r','s','p']
            return random.choice(letters)
        computer_play = randomrps()
        print("The computer chose: {}".format(computer_play))
        if play == computer_play:
            print("Its a tie!")
            print("Would you like to play again?")
            again = input("Please enter Yes or No: ")
            if again.lower() == 'yes':
                playing = True
            elif again.lower() == 'no':
                break
            else:
                while again.lower() != 'yes' or again.lower() != 'no':
                    again = input("Enter Yes or No ")
        if play == 'r' and computer_play == 's':
            print("Rock beats Scissors! You win!")
            print("Would you like to play again?")
            again = input("Please enter Yes or No: ")
            if again.lower() == 'yes':
                playing = True
            elif again.lower() == 'no':
                break
            else:
                while again.lower() != 'yes' or again.lower() != 'no':
                    again = input("Enter Yes or No ")
        if play == 'r' and computer_play == 'p':
            print("Paper beats Rock! You lose!")
            print("Would you like to play again?")
            again = input("Please enter Yes or No: ")
            if again.lower() == 'yes':
                playing = True
            elif again.lower() == 'no':
                break
            else:
                while again.lower() != 'yes' or again.lower() != 'no':
                    again = input("Enter Yes or No ")
        if play == 's' and computer_play == 'p':
            print("Scissors beats Paper! You win!")
            print("Would you like to play again?")
            again = input("Please enter Yes or No: ")
            if again.lower() == 'yes':
                playing = True
            elif again.lower() == 'no':
                break
            else:
                while again.lower() != 'yes' or again.lower() != 'no':
                    again = input("Enter Yes or No ")
        if play == 's' and computer_play == 'r':
            print("Rock beats Scissors! You lose!")
            print("Would you like to play again?")
            again = input("Please enter Yes or No: ")
            if again.lower() == 'yes':
                playing = True
            elif again.lower() == 'no':
                break
            else:
                while again.lower() != 'yes' or again.lower() != 'no':
                    again = input("Enter Yes or No ")
        if play == 'p' and computer_play == 'r':
            print("Paper beats Rock! You win!")
            print("Would you like to play again?")
            again = input("Please enter Yes or No: ")
            if again.lower() == 'yes':
                playing = True
            elif again.lower() == 'no':
                break
            else:
                while again.lower() != 'yes' or again.lower() != 'no':
                    again = input("Enter Yes or No ")
        if play == 'p' and computer_play == 's':
            print("Scissors beats paper! You lose!")
            print("Would you like to play again?")
            again = input("Please enter Yes or No: ")
            if again.lower() == 'yes':
                playing = True
            elif again.lower() == 'no':
                break
            else:
                while again.lower() != 'yes' or again.lower() != 'no':
                    again = input("Enter Yes or No ")
    else:
        while play != 'r' and play != 's' and play != 'p':
            play = input("Please enter 'r', 'p', or 's': ")
    