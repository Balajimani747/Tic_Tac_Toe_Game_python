play = [['', '', ''],
        ['', '', ''],
        ['', '', '']]

d = []
count1 = 0
count2 = 0

def wining(play):
    for row in play:
        if row[0]==row[1]==row[2] and row[0]!='':
            return True
        break
    for col in range(3):
        if play[0][col]==play[1][col]==play[2][col] and play[0][col]!='':
            return True
        break
    if play[0][0]==play[1][1]==play[2][2] and play[0][0]!='':
        return True
    return False    

def display_board(play):
    for i in range(3):
        print("\n----------")
        for j in range(3):
            if j == 0:
                print("|", end=" ")
            print(play[i][j], end=" | ")
    print("\n----------")

con = True
while count1<9 and count2<9:
        if count1 < 6 and count2 < 6:
            x = int(input("Enter X turn (0-8): "))
            if x in d:
                print("Already Position Taken-You lost your Turn")
            else:
                if 0 <= x < 3:
                    play[0][x] = "X"
                    display_board(play)
                elif 3 <= x < 6:
                    play[1][x - 3] = "X"
                    display_board(play)
                elif 6 <= x < 9:
                    play[2][x - 6] = "X"
                    display_board(play)
            d.append(x)
            count1 += 1
            print(count1)
        wincheck=wining(play)
        if wincheck==True:
            print("Player X win")
      

        if count1 < 5 and count2 < 5: 
            o = int(input("Enter O turn (0-8): "))
            if o in d:
                print("Already Position Taken-You lost your Turn")
            else:
                if 0 <= o < 3:
                    play[0][o] = "O"
                    display_board(play)
                elif 3 <= o < 6:
                    play[1][o - 3] = "O"
                    display_board(play)
                elif 6 <= o < 9:
                    play[2][o - 6] = "O"
                    display_board(play)
            d.append(o)
            count2 += 1
            print(count2)
        wincheck1=wining(play)
        if wincheck1==True:
            print("Player O win")
if count1 == 9 and count2 == 9:
    print("Match Draw")
