import tkinter as tk 
#make empty window
root=tk.Tk()
# put screenwidth and 
root.geometry("700x640")
#veriable for stalled
# p is the player
# w are the walls
#g is goal for player move to reach
#e is enemies
#c stand for score
grid = [
    [0, 0, 0 , 0 , 0 , 0 , 0 , 0, 0 , 0 , 0 , 0, 0 , 0 ,0],
    ["p","w", 0 , 0 , "c" , 0 , 0 ,"c", 0 , 0 , 0 ,"c", 0 , 0 ,"c"],
    [ 0 ,"w", 0 ,"w","w","w","w","w","w","w","w","w","w","w", 0 ],
    [ 0 ,"w", 0 ,"e" , 0 ,"w", 0 , 0 , 0 , "e" , 0 , 0 , 0 ,"w", 0],
    ["c" ,"w", 0 , 0 ,"e", 0 ,"c" , 0 ,"w", 0 ,"w", 0 ,"w","w","c"],
    [ 0 ,"w","w", 0 ,"w","w","w","w","w","c","w", 0 , 0 ,"w", 0 ],
    [ 0 ,"c", 0 ,"c" ,"c" , 0 , 0 , 0 ,"c",0 ,"w","w","c","w","c"],
    ["w","w","w", 0 ,"w","w","w","w","w", 0 , 0 , 0 , "c" , 0 ,"c"],
    [ 0 ,"c" , 0 , 0 ,"w", 0 ,"c" , 0 ,"w","w","w","w","w","w","w"],
    ["c" ,"w", 0 , 0 ,"w", 0 ,"w", 0 ,"e" , 0 ,"c", 0 , 0 ,"e" , 0],
    [ 0 ,"w", 0 ,"w","w", "c" ,"w","w","w","w","w","w","w","w", 0 ],
    [ 0 ,"w","c","w","w", 0 , 0 ,"c", 0 , 0 ,"e", 0 ,"e" , 0 , 0 ],
    ["c" ,"w", 0 , 0 ,"w","w","w", 0 ,"w","w","w", 0 ,"w","w","w"],
    [ 0 ,"w", 0 ,"c", 0 , 0 ,"w","c","w", 0 ,"w","c","w", 0 ,"g"],
    [ 0 ,"w","w","w","w","w","w", 0 ,"c", 0 ,"w", 0 ,"w", 0 ,"w"],
    ["c" , 0 ,"c", 0 ,"c", 0 ,"c", 0 ,"w","w","w","c", 0 ,"c","w"]
]
frame=tk.Frame()
frame.master.title("hello gamer")
#score
score=0
# square size
square_size=640/len(grid)
#Function
img = tk.PhotoImage(file="mario.png")
img1=tk.PhotoImage(file='flagGreen_down.png')
coinGold=tk.PhotoImage(file='coinGold.png')
img3=tk.PhotoImage(file='enemy1.gif')
wall=tk.PhotoImage(file='walls.png')
champoin=tk.PhotoImage(file='champoin.png')
lost=tk.PhotoImage(file="Lost.png")
def drawGrid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]=="p":
                # player=canvas.create_rectangle(row*square_size,col*square_size,2*square_size*row,2*square_size*col,outline="white",fill="white")
                player = canvas.create_image(50+col*square_size,row*square_size, image=img, anchor='nw')
            elif grid[row][col]=="w":
                wells=canvas.create_image(50+col*square_size,row*square_size, image=wall, anchor='nw')
            elif grid[row][col]=="g":
                goal=canvas.create_image(50+col*square_size,row*square_size, image=img1, anchor='nw')
            elif grid[row][col]=="c":
                # background=canvas.create_rectangle(row*square_size,col*square_size,2*square_size*row,2*square_size*col,outline="white",fill="white")
                score=canvas.create_image(50+col*square_size,row*square_size,image=coinGold,anchor='nw')
            elif grid[row][col]=="e":
                # background=canvas.create_rectangle(row*square_size,col*square_size,2*square_size*row,2*square_size*col,outline="white",fill="white")
                enemies = canvas.create_image(50+col*square_size,row*square_size, image=img3, anchor='nw')

            # else:
            #     player=canvas.create_rectangle(row*square_size,col*square_size,2*square_size*row,2*square_size*col,outline="",fill="white")
    
def getPositionPlayer(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]=="p":
                indexX=row
                indexY=col
    return([indexX, indexY])
def moveToLeft(event):
    global grid, score
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if  indexY>0:
        if grid[indexX][indexY-1] == 0:
            grid[indexX][indexY]=0
            grid[indexX][indexY-1]="p"
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX][indexY-1]=="c":
            grid[indexX][indexY]=0
            grid[indexX][indexY-1]="p"
            score += 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX][indexY-1]=="e":
            canvas.delete('all')
            canvas.create_image(200,200, image=lost, anchor='nw')
            canvas.create_text(310,100,text="You lost!",font=("arail",30))
def moveToRight(event):
    global grid, score
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if indexY<len(grid[0])-1:
        if grid[indexX][indexY+1]==0:
            grid[indexX][indexY]=0
            grid[indexX][indexY+1]="p"
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX][indexY+1]=="g":
            canvas.delete('all')
            canvas.create_image(200,200, image=champoin, anchor='nw')
            canvas.create_text(310,100,text="You win!",font=("arail",30))
        elif grid[indexX][indexY+1]=="c":
            grid[indexX][indexY]=0
            grid[indexX][indexY+1]="p"
            score += 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX][indexY+1]=="e":
            canvas.delete('all')
            canvas.create_image(200,200, image=lost, anchor='nw')
            canvas.create_text(310,100,text="You lost!",font=("arail",30))
def moveToUp(event):
    global grid, score
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if  indexX>1:
        if   grid[indexX-1][indexY]==0:
            grid[indexX][indexY]=0
            grid[indexX-1][indexY]="p"
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX-1][indexY]=="c":
            grid[indexX][indexY]=0
            grid[indexX-1][indexY]="p"
            score += 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX-1][indexY]=="e":
            canvas.delete('all')
            canvas.create_image(200,200, image=lost, anchor='nw')
            canvas.create_text(310,100,text="You lost!",font=("arail",30))
def moveToDown(event):
    global grid, score
    indexX = getPositionPlayer(grid)[0]
    indexY = getPositionPlayer(grid)[1]
    if indexX<len(grid)-1:
        if  grid[indexX+1][indexY]==0:
            grid[indexX][indexY]=0
            grid[indexX+1][indexY]="p"
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX+1][indexY]=="c":
            grid[indexX][indexY]=0
            grid[indexX+1][indexY]="p"
            score += 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX+1][indexY]=="e":
            canvas.delete('all')
            canvas.create_image(200,200, image=lost, anchor='nw')
            canvas.create_text(310,100,text="You lost!",font=("arail",30))
canvas=tk.Canvas(root)
def borderAndScore():
    point=canvas.create_text(350,20,text=("score : "+str(score)),font=("Comic Sans",15),fill='blue')
    left = canvas.create_line(47, 40, 47, 640, fill='black')
    top = canvas.create_line(47, 40, 653, 40, fill='black')
    right = canvas.create_line(653, 40, 653, 640, fill='black')
    bottom = canvas.create_line(47, 637, 653, 637, fill='black')
root.bind("<Left>",moveToLeft)     #move to left
root.bind("<Right>",moveToRight)   #move to right
root.bind("<Up>",moveToUp)         #move to up
root.bind("<Down>",moveToDown)     #move to down
drawGrid()
borderAndScore()
#create button

canvas.pack(expand=True,fill='both')
root.resizable(False,False)
root.mainloop()