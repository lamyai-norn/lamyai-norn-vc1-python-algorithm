import tkinter as tk 
import winsound
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

# Play the sound
grid = [
    [ 0 ,  0,  0 , 0 , 0 , 0 , 0 , 0,  0 , 0 , 0 , 0,  0 , 0 ,  0],
    ["p", "w", 0 , 0 ,"c","e" ,0 ,"c", 0 ,"c" ,0 ,"c", 0 ,"e" ,"c"],
    [ 0 , "w", 0 ,"w","w","w","w","w","w","w","w","w","w","w",  0],
    [ 0 , "w", 0 ,"e" ,0 ,"w", 0 ,"e" ,0 ,"c" ,0 ,"e" ,0 ,"w",  0],
    ["c", "w", 0 , 0 ,"e", 0 ,"c" ,0 ,"w", 0 ,"w", 0 ,"w","w", "c"],
    [ 0 , "w","w", 0 ,"w","w","w","w","w","c","w", 0 , 0 ,"w", "e"],
    ["e", "c", 0 ,"c","c" ,0 ,"e" ,0 ,"c", 0 ,"w","w","c","w", "c"],
    ["w", "w","w", 0 ,"w","w","w","w","w", 0 , 0 , 0 ,"c" ,0 , "c"],
    [ 0 , "c" ,0 ,"c" ,"w", 0 ,"c" ,0 ,"w","w","w","w","w","w",  0],
    ["c", "w","e" ,0 ,"w", 0 ,"w", 0 ,"e" ,0 ,"c", 0 , 0 ,"c" , 0],
    [ 0 , "w", 0 ,"w","w","c","w","w","w","w","w","w","w","w", "w"],
    [ 0, "w","c","w","w", 0 , 0 ,"c", 0 , 0 ,"e", 0 ,"c" ,0 ,  0],
    [ 0, "w","c","c" ,"w","w","w","c","w","w","w", 0 ,"w","w","w"],
    [ 0 , "w","e" ,"c", 0 , 0 ,"w","c","w","c","w", 0,"w", 0 , "g"],
    ["c" ,"w","w","w","w","w","w","e","c", 0,"w",  0, "w" ,0 , "w"],
    ["c",  0 ,"c", 0 ,"e", 0 ,"c", 0 ,"w","w","w","c", 0 , 0, "w"]
]
frame=tk.Frame()
frame.master.title("hello gamer")
#score
score=0
# life of player
life=5
# square size
square_size=640/len(grid)
#image
img = tk.PhotoImage(file="mario.png")
img1=tk.PhotoImage(file='flagGreen_down.png')
coinGold=tk.PhotoImage(file='coinGold.png')
img3=tk.PhotoImage(file='enemy1.gif')
wall=tk.PhotoImage(file='walls.png')
champoin=tk.PhotoImage(file='champoin.png')
lost=tk.PhotoImage(file="Lost.png")
#function
def drawGrid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]=="p":
                player = canvas.create_image(50+col*square_size,row*square_size, image=img, anchor='nw')
            elif grid[row][col]=="w":
                wells=canvas.create_image(50+col*square_size,row*square_size, image=wall, anchor='nw')
            elif grid[row][col]=="g":
                goal=canvas.create_image(50+col*square_size,row*square_size, image=img1, anchor='nw')
            elif grid[row][col]=="c":
                score=canvas.create_image(50+col*square_size,row*square_size,image=coinGold,anchor='nw')
            elif grid[row][col]=="e":
                enemies = canvas.create_image(50+col*square_size,row*square_size, image=img3, anchor='nw')
def getPositionPlayer(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]=="p":
                indexX=row
                indexY=col
    return([indexX, indexY])
def moveToLeft(event):
    global grid, score,life
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
            winsound.PlaySound("coin2.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            score += 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX][indexY-1]=="e":
            winsound.PlaySound("hurt.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[indexX][indexY]=0
            grid[indexX][indexY-1]="p"
            life -= 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
            if life==-1:
                canvas.delete('all')
                canvas.create_image(250,200, image=lost, anchor='nw')
                canvas.create_text(360,100,text="You lost!",font=("arail",30))
                winsound.PlaySound("lose4.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def moveToRight(event):
    global grid, score,life
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
            if score>20:
                canvas.delete('all')
                canvas.create_image(250,200, image=champoin, anchor='nw')
                canvas.create_text(360,100,text="You win!",font=("arail",30))
                winsound.PlaySound("win.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            else:
                canvas.delete('all') 
                canvas.create_text(360,250,text="You lost!",font=("arail",20))
                canvas.create_text(360,300,text="Not enough score.",font=("arail",20))
                winsound.PlaySound("lose4.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif grid[indexX][indexY+1]=="c":
            grid[indexX][indexY]=0
            grid[indexX][indexY+1]="p"
            winsound.PlaySound("coin2.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            score += 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX][indexY+1]=="e":
            winsound.PlaySound("hurt.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[indexX][indexY]=0
            grid[indexX][indexY+1]="p"

            life -= 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
            if life==-1:
                canvas.delete('all')
                canvas.create_image(250,200, image=lost, anchor='nw')
                canvas.create_text(360,100,text="You lost!",font=("arail",30))
                winsound.PlaySound("lose4.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def moveToUp(event):
    global grid, score,life
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
            winsound.PlaySound("coin2.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            score += 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX-1][indexY]=="e":
            winsound.PlaySound("hurt.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[indexX][indexY]=0
            grid[indexX-1][indexY]="p"
            life -= 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
            if life==-1:
                canvas.delete('all')
                canvas.create_image(250,200, image=lost, anchor='nw')
                canvas.create_text(360,100,text="You lost!",font=("arail",30))
                winsound.PlaySound("lose4.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def moveToDown(event):
    global grid, score,life
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
            winsound.PlaySound("coin2.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            score += 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
        elif grid[indexX+1][indexY]=="e":
            winsound.PlaySound("hurt.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            grid[indexX][indexY]=0
            grid[indexX+1][indexY]="p"
            life -= 1
            canvas.delete('all')
            drawGrid()
            borderAndScore()
            if life==-1:
                canvas.delete('all')
                canvas.create_image(250,200, image=lost, anchor='nw')
                canvas.create_text(360,100,text="You lost!",font=("arail",30))
                winsound.PlaySound("lose4.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
canvas=tk.Canvas(root)
def borderAndScore():
    point=canvas.create_text(250,20,text=("score : "+str(score)),font=("Comic Sans",15),fill='blue')
    lifePlayer=canvas.create_text(420,20,text=("life of Player: "+str(life)),font=("Comic Sans",15),fill='blue')
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
canvas.pack(expand=True,fill='both')
root.resizable(False,False)
root.mainloop()