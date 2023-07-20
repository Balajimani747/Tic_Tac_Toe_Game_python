


def demoboard():
    print("Game Rules: ")
    print(" @ Players should take turns, with one player using 'X' markers and the other using 'O' markers.\n", 
      "@ The game should accurately detect winning conditions, such as when a player has three of their markers in a row, column, or diagonal\n",
      "@ If all cells are occupied and no player has won, the game should declare a draw.")

    print("\nPlaying Bord of Tic Tac Toe!.Player refernece for position finding",end="")
    
    playground=[[0,1,2],
                [3,4,5],
                [6,7,8]]
    
    for i in range(3):
        print("\n-------------")
        for j in range(3):  
            if j==0:
                print("|",end=" ")
            print(playground[i][j],end=" | ")
    print("\n-------------")
    
def gamebord():
    playground =[["","",""],
                 ["","",""],
                 ["","",""]]
    for i in range(3):
        print("\n----------")
        for j in range(3):  
            if j==0:
                print("|",end=" ")
            print(playground[i][j],end=" | ")
    print("\n----------")
    
    x=int(input("Player X-Turn Enter 0-8: "))
    playground[2][2] = str(x)
gamebord()

    
    
########################################################################
print("Welcome To Tic Tac Toe Game\n")


demoboard()
gamebord()

# yes=input("Ready to Start Game (y/n): ")
# if (yes=='y' or yes=='Y'):
#     print("Game Start")
# else:
#     print("Game Exit")
    



    