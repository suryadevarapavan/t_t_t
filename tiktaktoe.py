import random
i=0
x=[]
o=[]
mg=[[8,1,6],[3,5,7],[4,9,2]]
print(mg)
A=[[1,2,3],[4,5,6],[7,8,9]]
i=0
def com():
    if i==1:
        print(random.choice())
    
def chk():
    if((sum(x)>=15 and len(x)>=3)and ("X"==A[0][0]==A[1][1]==A[2][2] or "X"==A[0][0]==A[0][1]==A[0][2] or "X"==A[1][0]==A[1][1]==A[1][2] or "X"==A[2][0]==A[2][1]==A[2][2] or "X"==A[0][0]==A[1][0]==A[2][0] or "X"==A[0][1]==A[1][1]==A[2][1] or "X"==A[0][2]==A[1][2]==A[2][2] or "X"==A[0][2]==A[1][1]==A[2][0])):
        print("PLAYER 1 WINS")
        return True
    elif ((sum(o)>=15 and len(o)>=3) and ("O"==A[0][0]==A[1][1]==A[2][2] or "O"==A[0][0]==A[0][1]==A[0][2] or "O"==A[1][0]==A[1][1]==A[1][2] or "O"==A[2][0]==A[2][1]==A[2][2] or "O"==A[0][0]==A[1][0]==A[2][0] or "O"==A[0][1]==A[1][1]==A[2][1] or "O"==A[0][2]==A[1][2]==A[2][2] or "O"==A[0][2]==A[1][1]==A[2][0] )):
        print("PLAYER 2 WINS")
        return True
def disp():
    print(A[0][0],"|",A[0][1],"|",A[0][2])
    print("----------")
    print(A[1][0],"|",A[1][1],"|",A[1][2])
    print("----------")
    print(A[2][0],"|",A[2][1],"|",A[2][2])
    print("___________")
def win(arr):
    cn=0
    for i in range(len(mg)):
        if(15-sum(arr) in mg[i]):
            cn=1
    if cn==1:
        print("CAN WIN")
        return True
    else:
        print("CANT WIN")
        return False
def it(a,arr):
    i=int(input("Enter Number Space:"))
    if i==1:
        A[0][0]=a
        arr.append(mg[0][0])
        mg[0][0] = None
    elif i==2:
        A[0][1]=a
        arr.append(mg[0][1])
        mg[0][1] = None
    elif i==3:
        A[0][2]=a
        arr.append(mg[0][2])
        mg[0][2] = None
    elif i==4:
        A[1][0]=a
        arr.append(mg[1][0])
        mg[1][0] = None
    elif i==5:
        A[1][1]=a
        arr.append(mg[1][1])
        mg[1][1] = None
    elif i==6:
        A[1][2]=a
        arr.append(mg[1][2])
        mg[1][2] = None
    elif i==7:
        A[2][0]=a
        arr.append(mg[2][0])
        mg[2][0] = None
    elif i==8:
        A[2][1]=a
        arr.append(mg[2][1])
        mg[2][1] = None
    elif i==9:
        A[2][2]=a
        arr.append(mg[2][2])
        mg[2][2] = None
while(1):
    disp()
    if i > 3:
        print("GAME 0VER")
        break
    it("X",x)
    #win(x)
    disp()
    if(chk()==True):
        break
    it("O",o)
    #win(o)
    disp()
    if(chk()):
        break
    i=+1
    #com()
        
