import random

moves = ['r', 'p', 's']
points = 0
player_wins = ['pr', 'sp', 'rs']

print("Let's play Rock, Paper, Scissors!")
print("When it is Your Move, enter-")
print("r for rock, p for paper, and s for scissors.")
print("Then I will do the same and we will see who wins!")
print("By the way, to quit the game, type q .")
print('This game starts.... NOW!!')

while True:
    player_move = input("Your move: ")
    computer_move = random.choice(moves)

    print("Computer: ", computer_move)

    if player_move == computer_move:
        print("It is a tie!")
        print("Let's play again!")

    elif player_move + computer_move in player_wins:
        print("You win!!")
        points = points + 1
        print("Let's play again!")

    else:
        print("Uh-oh You lose!")
        print("Let's play again!")

    if player_move == 'q':
        print("Number of points:", points)
        print("Bye!")
        break