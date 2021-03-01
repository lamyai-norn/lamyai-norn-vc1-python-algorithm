import tkinter as tk 
#make empty window
root=tk.Tk()
# put screenwidth and 
root.geometry("640x640")
#veriable for stalled
# p is the player
# w are the walls
#g is goal for player move to reach
#e is enemies
grid = [
    ["p","w", 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
    [ 0 ,"w", 0 ,"w","w","w","w","w","w","w","w","w","w","w", 0 ],
    [ 0 ,"w", 0 , 0 , 0 ,"w", 0 , 0 , 0 , 0 , 0 , 0 , 0 ,"w", 0 ],
    [ 0 ,"w", 0 , 0 ,"e", 0 , 0 , 0 ,"w", 0 ,"w", 0 ,"w","w", 0 ],
    [ 0 ,"w","w", 0 ,"w","w","w","w","w", 0 ,"w", 0 , 0 ,"w", 0 ],
    [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,"w","w", 0 ,"w", 0 ],
    ["w","w","w", 0 ,"w","w","w","w","w", 0 , 0 , 0 , 0 , 0 , 0 ],
    [ 0 , 0 , 0 , 0 ,"w", 0 , 0 , 0 ,"w","w","w","w","w","w","w"],
    [ 0 ,"w", 0 , 0 ,"w", 0 ,"w", 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
    [ 0 ,"w", 0 ,"w","w", 0 ,"w","w","w","w","w","w","w","w", 0 ],
    [ 0 ,"w", 0 ,"w","w", 0 , 0 , 0 , 0 , 0 ,"e", 0 , 0 , 0 , 0 ],
    [ 0 ,"w", 0 , 0 ,"w","w","w", 0 ,"w","w","w", 0 ,"w","w","w"],
    [ 0 ,"w", 0 , 0 , 0 , 0 ,"w", 0 ,"w", 0 ,"w", 0 ,"w", 0 ,"g"],
    [ 0 ,"w","w","w","w","w","w", 0 , 0 , 0 ,"w", 0 ,"w", 0 ,"w"],
    [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,"w","w","w", 0 , 0 , 0 ,"w"]
]
frame=tk.Frame()
frame.master.title("hello gamer")

# square size
square_size=645/len(grid)
#Function
img = tk.PhotoImage(file="mario.png")
img1=tk.PhotoImage(file='flagGreen_down.png')
# img2=tk.PhotoImage(file='C:\\Users\\student\\Desktop\\lamyai-norn-vc1-python-algorithm\\champion.jpg')
img3=tk.PhotoImage(file='enemy1.gif')
wall=tk.PhotoImage(file='walls.png')
champoin=tk.PhotoImage(file='champoin.png')
lost=tk.PhotoImage(file="Lost.png")
def drawGrid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[col][row]=="p":
                player=canvas.create_rectangle(row*square_size,col*square_size,43+square_size*row,43+square_size*col,outline="white",fill="white")
                player = canvas.create_image(row*square_size,col*square_size, image=img, anchor='nw')
            elif grid[col][row]=="w":
                player=canvas.create_image(row*square_size,col*square_size, image=wall, anchor='nw')
            elif grid[col][row]=="g":
                player=canvas.create_image(row*square_size,col*square_size, image=img1, anchor='nw')
            elif grid[col][row]=="e":
                player=canvas.create_rectangle(row*square_size,col*square_size,43+square_size*row,43+square_size*col,outline="white",fill="white")
                enemies = canvas.create_image(row*square_size,col*square_size, image=img3, anchor='nw')
                print(row*square_size,col*square_size)
                # indexEnemies=getindexenemy(enemies)
            else:
                player=canvas.create_rectangle(row*square_size,col*square_size,43+square_size*row,43+square_size*col,outline="",fill="white")
# def getindexenemy(index):
    
def getPositionPlayer(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[col][row]=="p":
                indexX=row
                indexY=col
    return([indexX, indexY])
def moveToLeft(event):
    global grid 
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if  indexX>0:
        if grid[indexY][indexX-1] == 0:
            grid[indexY][indexX]=0
            grid[indexY][indexX-1]="p"
            drawGrid()
        elif grid[indexY][indexX-1]=="e":
            canvas.delete('all')
            canvas.create_image(200,200, image=lost, anchor='nw')
            canvas.create_text(310,100,text="You lost!",font=("arail",30))
def moveToRight(event):
    global grid
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if indexX<len(grid)-1:
        if grid[indexY][indexX+1]==0:
            grid[indexY][indexX]=0
            grid[indexY][indexX+1]="p"
            drawGrid()
        elif grid[indexY][indexX+1]=="g":
            canvas.delete('all')
            canvas.create_image(200,200, image=champoin, anchor='nw')
            canvas.create_text(310,100,text="You win!",font=("arail",30))
        elif grid[indexY][indexX+1]=="e":
            canvas.delete('all')
            canvas.create_image(200,200, image=lost, anchor='nw')
            canvas.create_text(310,100,text="You lost!",font=("arail",30))
def moveToUp(event):
    global grid
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if  indexY>0:
        if   grid[indexY-1][indexX]==0:
            grid[indexY][indexX]=0
            grid[indexY-1][indexX]="p"
            drawGrid()
        elif grid[indexY-1][indexX]=="e":
            canvas.delete('all')
            canvas.create_image(200,200, image=lost, anchor='nw')
            canvas.create_text(310,100,text="You lost!",font=("arail",30))
def moveToDown(event):
    global grid
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if indexY<len(grid)-1:
        if  grid[indexY+1][indexX]==0:
            grid[indexY][indexX]=0
            grid[indexY+1][indexX]="p"
            drawGrid()
        elif grid[indexY+1][indexX]=="e":
            canvas.delete('all')
            canvas.create_image(200,200, image=lost, anchor='nw')
            canvas.create_text(310,100,text="You lost!",font=("arail",30))
canvas=tk.Canvas(root,)
root.bind("<Left>",moveToLeft)#move to left
root.bind("<Right>",moveToRight)#move to right
root.bind("<Up>",moveToUp)#move to up
root.bind("<Down>",moveToDown)#move to down
drawGrid()
canvas.pack(expand=True,fill='both')
root.resizable(False,False)
root.mainloop()