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
grid = [["p",0,"w",0,0,0,0,0,0], [0,0,"w",0,"w","w","w","w",0],[0,0,"w",0,0,0,0,0,0], ["e",0,0,0,0,0,0,"w",0], [0,0,"w","w","w","w",0,"w",0], ["e",0,0,0,0,0,0,"w",0], ["w","w","w",0,"w","w","w","w",0], ["e",00,0,0,0,0,0,0,0], [0,0,0,"w","w","w","w","w","g"]]
frame=tk.Frame()
frame.master.title("hello gamer")

# square size
square_size=630/len(grid)
#Function
img = tk.PhotoImage(file='C:\\Users\\student\\Desktop\\lamyai-norn-vc1-python-algorithm\\mario2.gif')
img1=tk.PhotoImage(file='C:\\Users\\student\\Desktop\\lamyai-norn-vc1-python-algorithm\\flagGreen_down.png')
# img2=tk.PhotoImage(file='C:\\Users\\student\\Desktop\\lamyai-norn-vc1-python-algorithm\\champion.jpg')
# img3=tk.PhotoImage(file='C:\\Users\\student\\Desktop\\lamyai-norn-vc1-python-algorithm\\enemy.jpg')
def drawGrid():
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]=="p":
                player = canvas.create_image(row*square_size,col*square_size, image=img, anchor='nw')
            elif grid[row][col]=="w":
                player=canvas.create_rectangle(row*square_size,col*square_size,70+square_size*row,70+square_size*col,outline="blue",fill="blue")
            elif grid[row][col]=="g":
                player=canvas.create_image(row*square_size,col*square_size, image=img1, anchor='nw')
            elif grid[row][col]=="e":
                enemies=canvas.create_oval(row*square_size,col*square_size,70+square_size*row,70+square_size*col,outline="red",fill="red")
                # enemies = canvas.create_image(row*square_size,col*square_size, image=img3, anchor='nw')
                # enemies = canvas.create_image(100,100, image=img3, anchor='nw')
            else:
                player=canvas.create_rectangle(row*square_size,col*square_size,70+square_size*row,70+square_size*col,outline="white",fill="white")
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
        if grid[indexX+1][indexY]=="g":
            canvas.delete('all')
            canvas.create_text(280,200,text="You are win!",font=("arail",30))
            # canvas.create_image(280,400, image=img2, anchor='nw')
            grid[indexX][indexY]=0
            grid[indexX+1][indexY]="p"
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