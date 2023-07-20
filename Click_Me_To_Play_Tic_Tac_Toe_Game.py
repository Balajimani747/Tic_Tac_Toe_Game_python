#------------------------------------------------------->(Game Rules)
def gamerules():
    print("\nWelcome To Tic Tac Toe Game")
    print("Game Rules: ")
    print(" @ Players should take turns, with one player using 'X' markers and the other using 'O' markers.\n", 
      "@ The game should accurately detect winning conditions, such as when a player has three of their markers in a row, column, or diagonal\n",
      "@ If all cells are occupied and no player has won, the game should declare a draw.\n",
      "@ If you enter a number that is already on the board, you will lose your current turn and have to wait for the next turn to make a move.")
    print("\nPlaying Bord of Tic Tac Toe!.Player refernece for position finding",end="")
    playground=[[0,1,2],
                [3,4,5],
                [6,7,8]]
    display(playground)
#----------------------------------------------------->(Diaplay Fuction)
def display(play):
    for i in range(3):
        print("\n------------")
        for j in range(3):
            if j == 0:
                print("|", end=" ")
            print(play[i][j], end=" | ")
    print("\n------------")
#------------------------------------------------------>(Game Winning Fuction)
def wining(play):
    for row in play:
        if row[0]==row[1]==row[2] and row[0]!='':
            return True
    for col in range(3):
        if play[0][col]==play[1][col]==play[2][col] and play[0][col]!='':
            return True
    if play[0][0]==play[1][1]==play[2][2] and play[0][0]!='':
        return True  
    if play[0][2] == play[1][1] == play[2][0] and play[0][2] != '':
        return True
    return False
#---------------------------------------------------------->(x-Player move)
def x_player():
    x = int(input("Enter X turn (0-8): "))
    if x in num:
        print("Already Position Taken-You lost your Turn")
    else:
        if 0 <= x < 3:
            play[0][x] ="X"
            display(play)
        elif 3 <= x < 6:
            play[1][x - 3] ="X"
            display(play)
        elif 6 <= x < 9:
            play[2][x - 6] ="X"
            display(play)
        num.append(x)
#---------------------------------------------------------->(y-Player move)
def o_player():
    o = int(input("Enter O turn (0-8): "))
    if o in num:
        print("Already Position Taken-You lost your Turn")
    else:
        if 0 <= o < 3:
            play[0][o] = "O"
            display(play)
        elif 3 <= o < 6:
            play[1][o - 3] = "O"
            display(play)
        elif 6 <= o < 9:
            play[2][o - 6] = "O"
            display(play)
        num.append(o)
#---------------------------------------------------------->(Main Fuction)
play = [['', '', ''],
        ['', '', ''],
        ['', '', '']]
num= []
count1 = 0
count2 = 0
gamerules()
while True:
    if count1<5 and count2 <4: 
        if count1 < 5 :
            x_player()
            wincheck=wining(play)
            if wincheck==True:
                print("PLAYER X WIN")
                break
        if count2 < 4: 
            o_player()
            count2 += 1
            wincheck1=wining(play)
            if wincheck1==True:
                print("PLAYER O WIN")
                break
    else:
        print("It's a GAME-DRAW!")

