play=[['','',''],
      ['','',''],
      ['','','']]

d=[]
s=[]
count1=0
count2=0

def display_board(play):
    for i in range(3):
        print("\n----------")
        for j in range(3):  
            if j==0:
                print("|",end=" ")
            print(play[i][j],end=" | ")
    print("\n----------")

con=True
while con==True:
    if count1<=3:
        x=int(input("Enter X turn(0-8): "))
        if x in d:
            print("Alreday Position Taken")
        else:
            if x>=0 and x<3:
                for i in range(0,4):
                    if x==i:
                        play[0][i]="X"
                        display_board(play)
            elif x>=3 and x<6:
                for i in range(3,7):
                    if x==i:
                        play[1][i-3]="X"
                        display_board(play)           
            elif x>=6 and x<9:
                for i in range(6,9):
                    if x==i:
                        play[2][i-6]="X"
                        display_board(play)                  
        d.append(x)
        count1=count1+1
    if count2<=3:
        o=int(input("Enter O turn(0-8): "))
        if o in d:
            print("Alreday Position Taken")
            
        else:
            if o>=0 and o<3:
                for i in range(0,4):
                    if o==i:
                        play[0][i]="O"
                        display_board(play)
            elif o>=3 and o<6:
                for i in range(3,7):
                    if o==i:
                        play[1][i-3]="O"
                        display_board(play)           
            elif o>=6 and o<9:
                for i in range(6,9):
                    if o==i:
                        play[2][i-6]="O"
                        display_board(play)                  
        s.append(o)
        count2=count2+1
    

# def winning():
#     win_lis=[[0,1,2],[0,2,1],[1,0,2][1,2,0],[2,0,1],[2,1,0],
#              [3,4,5],[3,5,4],[4,3,5],[4,5,3],[5,3,4][5,4,2],
#              [6,7,8],[6,8,7],[7,6,8][7,8,6],[8,6,7],[8,7,6],
#              ]
    