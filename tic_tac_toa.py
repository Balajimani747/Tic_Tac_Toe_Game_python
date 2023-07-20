# print("Welcome to Tic Tac Toe Game")

# board = [[' ', ' ', ' '],
#          [' ', ' ', ' '],
#          [' ', ' ', ' ']]

# # Function to display the board
# def display_board():
#     for row in board:
#         print('|'.join(row))
#         print('-' * 5)
# #display_board()
# Method 1: Using nested lists (lists of lists)
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# a=len(matrix)
# b=len(matrix[0])
# print(a)  
# print(b)
# Method 2: Using NumPy
# import numpy as np

# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])

# # Accessing elements of the matrix
# print(matrix)  # Output: 1

ev= [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
      ]
col=len(ev)
row=len(ev[0])
for i in range(col):
    print("|")
    for j in range(row):
        #print(ev[j])
        print("-----------------")
     


