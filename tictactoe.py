print('TIC TAC TOE Game!')
print('\u00a9 Dimas Fakhri Arsaputra 2020')
print('arsaputradimas@yahoo.com\n')

def reset_board(board):
    for i in range(1,10):
        board[str(i)]=' '

        
def print_board(board):
    print(board['1']+'|'+board['2']+'|'+board['3'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['7']+'|'+board['8']+'|'+board['9'])

def game():
    print('For the game, we use the following coordinates for the boxes:')
    board = {'1': '1' , '2': '2' , '3': '3' ,'4': '4' , '5': '5' , '6': '6' ,'7': '7' , '8': '8' , '9': '9' }
    print_board(board)
    print('\n')
    playing_type=input('1-player or 2-player? (1P/2P)')
    while playing_type!='1P' and playing_type!='2P':
        playing_type=input('Please type \'1P\' for 1-player mode or \'2P\' for 2-player mode!')
    if playing_type=='2P':
        reset_board(board)
        count=0
        player='X'
        print_board(board)
        for i in range(10):
            count+=1
            if count%2==1:
                player='X'
            else:
                player='O'
            print("It's "+player+"'s Turn!")
            pos=input('Where to move? (1-9)')
            while True:
                if int(pos)<=9 and int(pos)>=1:
                    break
                else:
                    pos=input('Invalid argument! Where to move? (1-9)')
            while True:
                if board[pos]==' ':
                    board[pos]=player
                    break
                else:
                    pos=input('That place is taken! Where to move? (1-9)')
            print_board(board)
            if count==9:
                again=input("It's a tie! Wanna play again? (y/n)")
                while again.lower().strip()!='y' and again.lower().strip()!='n':
                    again=input("Type 'y' for yes and 'n' for no!")
                if again.lower().strip()=='y':
                    game()
                else:
                    break
            if count>=5:
                if board['1']==board['2']==board['3']!=' ':
                    print(player+' wins!')
                    again=input('Wanna play again? (y/n)')
                    while again.lower().strip()!='y' and again.lower().strip()!='n':
                        again=input("Type 'y' for yes and 'n' for no!")
                    if again.lower().strip()=='y':
                        game()
                    else:
                        break
                if board['4']==board['5']==board['6']!=' ':
                    print(player+' wins!')
                    again=input('Wanna play again? (y/n)')
                    while again.lower().strip()!='y' and again.lower().strip()!='n':
                        again=input("Type 'y' for yes and 'n' for no!")
                    if again.lower().strip()=='y':
                        game()
                    else:
                        break
                if board['7']==board['8']==board['9']!=' ':
                    print(player+' wins!')
                    again=input('Wanna play again? (y/n)')
                    while again.lower().strip()!='y' and again.lower().strip()!='n':
                        again=input("Type 'y' for yes and 'n' for no!")
                    if again.lower().strip()=='y':
                        game()
                    else:
                        break
                if board['1']==board['4']==board['7']!=' ':
                    print(player+' wins!')
                    again=input('Wanna play again? (y/n)')
                    while again.lower().strip()!='y' and again.lower().strip()!='n':
                        again=input("Type 'y' for yes and 'n' for no!")
                    if again.lower().strip()=='y':
                        game()
                    else:
                        break
                if board['2']==board['5']==board['8']!=' ':
                    print(player+' wins!')
                    again=input('Wanna play again? (y/n)')
                    while again.lower().strip()!='y' and again.lower().strip()!='n':
                        again=input("Type 'y' for yes and 'n' for no!")
                    if again.lower().strip()=='y':
                        game()
                    else:
                        break
                if board['3']==board['6']==board['9']!=' ':
                    print(player+' wins!')
                    again=input('Wanna play again? (y/n)')
                    while again.lower().strip()!='y' and again.lower().strip()!='n':
                        again=input("Type 'y' for yes and 'n' for no!")
                    if again.lower().strip()=='y':
                        game()
                    else:
                        break
                if board['1']==board['5']==board['9']!=' ':
                    print(player+' wins!')
                    again=input('Wanna play again? (y/n)')
                    while again.lower().strip()!='y' and again.lower().strip()!='n':
                        again=input("Type 'y' for yes and 'n' for no!")
                    if again.lower().strip()=='y':
                        game()
                    else:
                        break
                if board['3']==board['5']==board['7']!=' ':
                    print(player+' wins!')
                    again=input('Wanna play again? (y/n)')
                    while again.lower().strip()!='y' and again.lower().strip()!='n':
                        again=input("Type 'y' for yes and 'n' for no!")
                    if again.lower().strip()=='y':
                        game()
                    else:
                        break
    if playing_type=='1P':
        reset_board(board)
        count=0
        player='X'
        print_board(board)
        #Unfinished
                
                
game()

print('Thanks for playing!')
            
            
            
            
        
        
    
