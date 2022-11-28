from tkinter import *
import random
import time

isInEditor = False
def loadLevel(filename):
    global level, levelr, levelname
    levelname = filename
    level = open(filename, "a")
    levelr = open(filename, "r")

class Ball:
    def __init__(self, canvas, color, x, y):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, x, y)
        self.x = -5
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        
        #self.sprite = canvas.create_image(200, 470, image=PhotoImage(file='/Users/thomasholmesland/Documents/Thor/Programmering/Skoleprosjekt 2022/src/assets/art/ball.png'))

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        self.pos = self.canvas.coords(self.id)
        #print(self.pos)
        self.physics(racket)
            
    def physics(self, racket):
        if self.pos[0] <= racket.pos[2]:
            if self.pos[3] >= racket.pos[1]:
                if self.pos[1] <= racket.pos[3]:
                    self.x = 10
                    self.y = 5
            
        if self.pos[0] <= 0:
            global isDead
            isDead = True
            
class Racket:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 25, 75, fill=color)
        self.canvas.move(self.id, 50, 140)
        self.x = 0
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.pos = self.canvas.coords(self.id)
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        self.pos = self.canvas.coords(self.id)
        if frame > 10:
            self.move()
        
    def move(self):
        if self.pos[1] < mouse_y - 37:
            self.y = 10
        if self.pos[1] > mouse_y - 37:
            self.y = -10
        #print(mouse_y, self.pos[1], frame)

class BallSpawner:
    def __init__(self):
        self.levela = level
        self.isInEditor = isInEditor
        #print(levelr.read())

        if isInEditor:
            canvas.bind_all('<KeyPress-Up>', self.writePos)

    def start(self):
        if isInEditor == False:
            self.read()

    def update(self):
        global levelr
        levelr = open(levelname, "r")

    def read(self):
        levelt = levelr.read()
        levelt = levelt.split()
        
        global balllist
        for i, num in enumerate(levelt):
            ball = Ball(canvas, 'red', (i * 100) + 600, num)
            balllist.append(ball)

    def write(self):
        pass

    def writePos(self, evt):
        pos = racket.pos[1] - 37
        print(pos)

        level.write(str(int(pos)) + " ")

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

mouse_x = 0
mouse_y = 0

frame = 0

def motion(event):
    global mouse_x, mouse_y
    mouse_x, mouse_y = event.x, event.y

tk.bind('<Motion>', motion)

balllist = []
def makeBalls(lstx, lsty):
    for i, num in enumerate(lstx):
        ball = Ball(canvas, 'red', num, lsty[i])
        balllist.append(ball)

def on_closing():
    level.close()
    levelr.close()
    tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_closing)

loadLevel("level1.txt")
isDead = False
ballspawner = BallSpawner()

racket = Racket(canvas, 'blue')
#ball = Ball(canvas, 'red', 500, 250)

#makeBalls([600, 700, 800, 900, 1000], 
#          [300, 250, 200, 150, 100])


ballspawner.start()
while 1:
    ballspawner.update()
    if isDead == False:
        racket.draw()
        #ball.draw()
        for ball in balllist:
            ball.draw()
    tk.update_idletasks()
    tk.update()
    frame += 1
    time.sleep(0.01)
