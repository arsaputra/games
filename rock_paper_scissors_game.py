from random import randint

Options= ["ROCK","PAPER","SCISSORS"]
print('Rock, Paper, Scissors game!')
while True:
    player=input('What is your choice?').upper().strip()
    if player not in Options:
        print('Invalid choice! Your possible choices are ROCK, PAPER, and SCISSORS')
    else:
        computer=Options[randint(0,2)]
        if player==computer:
            print('Your choice: '+player)
            print('Computer: '+computer)
            choice=input('It\'s a tie! Want to play again? :) YES/NO')
            if choice.upper().strip()=='YES':
                continue
            else:
                break
        if player=='ROCK' and computer=='PAPER':
            print('Your choice: ROCK')
            print('Computer: PAPER')
            choice=input('You lost! Give another shot? :) YES/NO')
            if choice.upper().strip()=='YES':
                continue
            else:
                break
        if player=='ROCK' and computer=='SCISSORS':
            print('Your choice: ROCK')
            print('Computer: SCISSORS')
            choice=input('You won! Play again? :) YES/NO')
            if choice.upper().strip()=='YES':
                continue
            else:
                break
        if player=='PAPER' and computer=='SCISSORS':
            print('Your choice: PAPER')
            print('Computer: SCISSORS')
            choice=input('You lost! Give another shot? :) YES/NO')
            if choice.upper().strip()=='YES':
                continue
            else:
                break
        if player=='PAPER' and computer=='ROCK':
            print('Your choice: PAPER')
            print('Computer: ROCK')
            choice=input('You won! Play again? :) YES/NO')
            if choice.upper().strip()=='YES':
                continue
            else:
                break
        if player=='SCISSORS' and computer=='ROCK':
            print('Your choice: SCISSORS')
            print('Computer: ROCK')
            choice=input('You lost! Give another shot? :) YES/NO')
            if choice.upper().strip()=='YES':
                continue
            else:
                break
        if player=='SCISSORS' and computer=='PAPER':
            print('Your choice: SCISSORS')
            print('Computer: PAPER')
            choice=input('You won! Play again? :) YES/NO')
            if choice.upper().strip()=='YES':
                continue
            else:
                break
        
print('Thanks for playing!')


