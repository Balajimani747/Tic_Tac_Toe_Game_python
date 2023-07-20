play = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]


def gamebord(args):
    playground = [["", "", ""],
                  ["", "", ""],
                  ["", "", ""]]

    for i in range(3):
        print("\n----------")
        for j in range(3):
            if j == 0:
                print("|", end=" ")
            print(args[i][j], end=" | ")
    print("\n----------")



#o=input("enter y tuen: ")
d=[]
con=True
while con==True:
    x=int(input("Enter x turn: "))
    d.append(x)
    if x==0:
        play[0][0]="X"
        gamebord(play)
        con=True
    elif x==1:
        play[0][1]="X"
        gamebord(play)
        con=True
    elif x==2:
        play[0][2]="x"
        gamebord(play)
        con=False
print(d)