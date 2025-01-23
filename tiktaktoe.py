p1=[]
p2=[]
mg=[[8,1,6],[3,5,7],[4,9,2]]
A=[[" "," "," "],[" "," "," "],[" "," "," "]]
i=0
def disp():
    print(A[0][0],"|",A[0][1],"|",A[0][2])
    print("----------")
    print(A[1][0],"|",A[1][1],"|",A[1][2])
    print("----------")
    print(A[2][0],"|",A[2][1],"|",A[2][2])

while(1):
    if(i>3):
        print("Game OVER")
        break;
    print("PLAYER_ONE")
    m=int(input("Enter value for m:"))
    n=int(input("Enter value for n:"))
    A[m-1][n-1]="X"
    disp()
    if( "X"==A[0][0]==A[1][1]==A[2][2] or "X"==A[0][0]==A[0][1]==A[0][2] or "X"==A[1][0]==A[1][1]==A[1][2] or "X"==A[2][0]==A[2][1]==A[2][2] or "X"==A[0][0]==A[1][0]==A[2][0] or "X"==A[0][1]==A[1][1]==A[2][1] or "X"==A[0][2]==A[1][2]==A[2][2]):
        print("Player 0NE Wins")
        break;
    print("PLAYER_TWO")
    m=int(input("Enter value for m:"))
    n=int(input("Enter value for n:"))
    A[m-1][n-1]="O"
    disp()
    if( "O"==A[0][0]==A[1][1]==A[2][2] or "O"==A[0][0]==A[0][1]==A[0][2] or "O"==A[1][0]==A[1][1]==A[1][2] or "O"==A[2][0]==A[2][1]==A[2][2] or "O"==A[0][0]==A[1][0]==A[2][0] or "O"==A[0][1]==A[1][1]==A[2][1] or "O"==A[0][2]==A[1][2]==A[2][2]):
        print("Player TW0 Wins")
        break;
    i=i+1

                 
