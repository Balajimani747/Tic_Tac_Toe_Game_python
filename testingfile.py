playground = [["", "", ""],
              ["", "", ""],
              ["", "", ""]]

x = int(input("Player X-Turn Enter 0-8: "))

# Convert the user input to a string before assigning it
playground[2][2] = str(x)

for i in range(3):
        print("\n----------")
        for j in range(3):  
            if j==0:
                print("|",end=" ")
            print(playground[i][j],end=" | ")
print("\n----------")

def df(a):
   for i in range(3):
        print("\n----------")
        for j in range(3):  
            if j==0:
                print("|",end=" ")
            print(a[i][j],end=" | ")
print("\n----------")

ds=[["",2,3],
    [4,3,2],
    [54,22,21]]
ds[0][0]=1
df(ds)