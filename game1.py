import tkinter as tk 
#make empty window
root=tk.Tk()
# put screenwidth and 
root.geometry("630x630")
#veriable for stalled
# p is the player
# w are the walls
#g is goal for player move to reach
#e is enemies
grid = [["p",0,"w",0,0,0,0,0,0], [0,0,"w",0,"w","w","w","w",0],[0,0,"w",0,0,0,0,0,0], ["e",0,0,0,0,0,0,"w",0], [0,0,"w","w","w","w",0,"w",0], [0,0,0,0,0,0,0,"w",0], ["w","w","w",0,"w","w","w","w",0], [0,0,0,0,0,0,0,0,0], [0,0,0,"w","w","w","w","w","g"]]
frame=tk.Frame()
frame.master.title("hello gamer")

# square size
square_size=630/len(grid)
#Function
root.imageLuigi = tk.PhotoImage(file=r'./mario2.gif')
def drawGrid():
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]=="p":
                player = canvas.create_image(row*square_size,col*square_size, image=root.imageLuigi, anchor='nw', tags="player")
                # player=canvas.create_rectangle(row*square_size,col*square_size,70+square_size*row,70+square_size*col,fill="black")
            elif grid[row][col]=="w":
                player=canvas.create_rectangle(row*square_size,col*square_size,70+square_size*row,70+square_size*col,fill="blue")
            elif grid[row][col]=="g":
                player=canvas.create_rectangle(row*square_size,col*square_size,70+square_size*row,70+square_size*col,fill="green")
            elif grid[row][col]=="e":
                enemies=canvas.create_oval(row*square_size,col*square_size,70+square_size*row,70+square_size*col,fill="green")
            else:
                player=canvas.create_rectangle(row*square_size,col*square_size,70+square_size*row,70+square_size*col,fill="white")
    return None

def getPositionPlayer(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]=="p":
                indexX=row
                indexY=col
    return([indexX, indexY])


def moveToLeft(event):
    global grid 
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if  indexX>0:
        if grid[indexX-1][indexY] == 0:
            grid[indexX][indexY]=0
            grid[indexX-1][indexY]="p"
            drawGrid()
    
def moveToRight(event):
    global grid
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if indexX<len(grid)-1:
        if grid[indexX+1][indexY]==0:
            grid[indexX][indexY]=0
            grid[indexX+1][indexY]="p"
            drawGrid()
def moveToUp(event):
    global grid
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if  indexY>0:
        if   grid[indexX][indexY-1]==0:
            grid[indexX][indexY]=0
            grid[indexX][indexY-1]="p"
            drawGrid()
def moveToDown(event):
    global grid
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if indexY<len(grid)-1:
        if  grid[indexX][indexY+1]==0:
            grid[indexX][indexY]=0
            grid[indexX][indexY+1]="p"
            drawGrid()
canvas=tk.Canvas(root,)
root.bind("<Left>",moveToLeft)#move to left
root.bind("<Right>",moveToRight)#move to right
root.bind("<Up>",moveToUp)#move to up
root.bind("<Down>",moveToDown)#move to down
drawGrid()
canvas.pack(expand=True,fill='both')
root.resizable(False,False)
root.mainloop()